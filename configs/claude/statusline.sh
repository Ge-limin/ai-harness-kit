#!/bin/bash
# Claude Code status line: dir | branch | model | Ctx:NN% | 5h:NN% (2h13m) 7d:NN% (3d4h)
# Reads the statusline JSON from stdin; every segment is omitted when its data is absent.

input=$(cat)

# One jq pass; missing values become empty strings. Fields are joined with \x1f, not a
# tab, because read collapses consecutive whitespace delimiters and would shift empty fields.
IFS=$'\x1f' read -r cwd model used remaining five five_reset week week_reset <<<"$(
  echo "$input" | jq -r '[
    .workspace.current_dir // "",
    .model.display_name // "",
    (.context_window.used_percentage // "" | if . == "" then . else round end),
    (.context_window.remaining_percentage // ""),
    (.rate_limits.five_hour.used_percentage // "" | if . == "" then . else round end),
    (.rate_limits.five_hour.resets_at // ""),
    (.rate_limits.seven_day.used_percentage // "" | if . == "" then . else round end),
    (.rate_limits.seven_day.resets_at // "")
  ] | map(tostring) | join("\u001f")'
)"

if [ -z "$used" ] && [ -n "$remaining" ]; then
  used=$(awk "BEGIN{printf \"%.0f\", 100-($remaining); exit}")
fi

branch=""
if [ -n "$cwd" ] && git -C "$cwd" --no-optional-locks rev-parse --git-dir >/dev/null 2>&1; then
  branch=$(git -C "$cwd" --no-optional-locks symbolic-ref --short HEAD 2>/dev/null ||
    git -C "$cwd" --no-optional-locks rev-parse --short HEAD 2>/dev/null)
fi

# Seconds until an epoch timestamp, formatted as 3d4h / 2h13m / 45m.
until_reset() {
  [ -z "$1" ] && return
  local s=$(( $1 - $(date +%s) ))
  [ "$s" -lt 0 ] && s=0
  local d=$(( s / 86400 )) h=$(( s % 86400 / 3600 )) m=$(( s % 3600 / 60 ))
  if [ "$d" -gt 0 ]; then printf '%dd%dh' "$d" "$h"
  elif [ "$h" -gt 0 ]; then printf '%dh%02dm' "$h" "$m"
  else printf '%dm' "$m"
  fi
}

SEP=$' \033[1;34m|\033[0m '
out=$'\033[0;36m'"$(basename "$cwd")"$'\033[0m'
[ -n "$branch" ] && out+="$SEP"$'\033[0;32m'"$branch"$'\033[0m'
out+="$SEP"$'\033[0;35m'"$model"$'\033[0m'
[ -n "$used" ] && out+="$SEP"$'\033[0;33m'"Ctx:${used}%"$'\033[0m'

limits=""
if [ -n "$five" ]; then
  limits="5h:${five}%"
  t=$(until_reset "$five_reset"); [ -n "$t" ] && limits+=" ($t)"
fi
if [ -n "$week" ]; then
  [ -n "$limits" ] && limits+=" "
  limits+="7d:${week}%"
  t=$(until_reset "$week_reset"); [ -n "$t" ] && limits+=" ($t)"
fi
[ -n "$limits" ] && out+="$SEP"$'\033[0;33m'"$limits"$'\033[0m'

printf '%s' "$out"
