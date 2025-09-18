# Claude Code Status Line Configuration

This directory contains the status line configuration for Claude Code, providing live data updates in the terminal.

## Files

- `settings.json` - Main Claude Code configuration file
- `statusline-command.sh` - Bash script that generates the status line with live data
- `test-statusline.sh` - Test script to verify status line functionality
- `README-statusline.md` - This documentation file

## Live Data Features

The status line displays the following live information:

1. **User & Hostname** - Current user and system hostname
2. **Directory Path** - Current directory relative to project root
3. **Git Status** - Current branch and file status indicators:
   - `*` = Modified files (uncommitted changes)
   - `+` = Untracked files
   - `^` = Staged changes
4. **Current Time** - Updates every time the status line refreshes
5. **Model Name** - Currently active Claude model
6. **System Load** - Current system load average
7. **Memory Usage** - Current memory usage

## Status Line Format

```
user@hostname /relative/path [branch *+^] [HH:MM:SS] Claude 3.5 Sonnet Load: 0.25 Mem: 2.1G
```

## Colors

- User@hostname: Dim gray
- Directory path: Blue
- Git info: Green
- Time: Dim gray  
- Model name: Magenta
- System info: Dim gray

## Testing

Run the test script to verify everything is working:

```bash
bash /workspaces/ioun-ai/.claude/test-statusline.sh
```

## Customization

To modify the status line, edit `statusline-command.sh`. The script receives JSON input from Claude Code via stdin containing workspace and model information.

## Troubleshooting

- Ensure `jq` is installed for JSON parsing
- Check that the script has execute permissions
- Verify the paths in `settings.json` are correct
- Test with the provided test script to identify issues