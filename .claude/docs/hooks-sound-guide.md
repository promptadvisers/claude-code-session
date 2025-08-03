# Claude Code Hooks Sound Guide

## Sound System Overview

Your Claude Code hooks now include audio feedback for different events, providing an immersive coding experience with distinctive sounds for each action.

## Hook Sound Mapping

### 🚀 **SessionStart** 
- **Sound**: Glass.aiff
- **When**: Claude Code session begins
- **Description**: Clear, welcoming chime

### 📝 **UserPromptSubmit**
- **Sound**: Pop.aiff  
- **When**: You submit a prompt
- **Description**: Subtle acknowledgment sound

### 🛠️ **ToolUse**
- **Sound**: Varies by tool type:
  - **Bash/Terminal**: Morse.aiff (command execution)
  - **MCP Servers**: Hero.aiff (enhanced capabilities)
  - **File Operations**: Tink.aiff (read/write/edit)
  - **Other Tools**: Purr.aiff (general tool usage)
- **When**: Any tool is executed
- **Description**: Contextual audio feedback

### 🛑 **Stop**
- **Sound**: Sosumi.aiff
- **When**: Session/conversation ends
- **Description**: Completion acknowledgment

### 🗜️ **PreCompact**
- **Sound**: Basso.aiff
- **When**: Before conversation compaction
- **Description**: Attention-getting warning tone

## macOS System Sounds Used

All sounds are built-in macOS system sounds located in `/System/Library/Sounds/`:

- **Glass.aiff** - Clear, welcoming startup
- **Pop.aiff** - Subtle acknowledgment 
- **Morse.aiff** - Command/terminal execution
- **Hero.aiff** - MCP server activation
- **Tink.aiff** - File operations
- **Purr.aiff** - General tool usage
- **Sosumi.aiff** - Session completion
- **Basso.aiff** - Warning/attention

## Customization Options

### Change Sounds
Edit any hook file and replace the sound name:
```bash
afplay /System/Library/Sounds/YourSound.aiff 2>/dev/null &
```

### Available System Sounds
Check all available sounds:
```bash
ls /System/Library/Sounds/
```

Common alternatives:
- **Blow.aiff** - Wind sound
- **Bottle.aiff** - Cork pop
- **Frog.aiff** - Ribbit sound
- **Funk.aiff** - Funky tone
- **Ping.aiff** - Network ping

### Disable Sounds
Comment out or remove the `afplay` line in any hook:
```bash
# afplay /System/Library/Sounds/Glass.aiff 2>/dev/null &
```

### Custom Sounds
Replace system sounds with your own files:
```bash
afplay /path/to/your/custom-sound.mp3 2>/dev/null &
```

## Cross-Platform Support

### Linux
Replace `afplay` with:
```bash
# Using paplay (PulseAudio)
paplay /usr/share/sounds/alsa/Front_Left.wav 2>/dev/null &

# Using aplay (ALSA)
aplay /usr/share/sounds/alsa/Front_Left.wav 2>/dev/null &
```

### Windows (Git Bash/WSL)
Replace `afplay` with:
```bash
# Using powershell
powershell -c "(New-Object Media.SoundPlayer 'C:\\Windows\\Media\\chimes.wav').PlaySync();" 2>/dev/null &
```

## Volume Control

Sounds play at system volume. To control hook sound volume:

1. **System Level**: Adjust macOS system volume
2. **Per-Hook**: Add volume control to `afplay`:
   ```bash
   afplay /System/Library/Sounds/Glass.aiff -v 0.5 2>/dev/null &
   ```
   (0.0 = silent, 1.0 = full volume)

## Troubleshooting

### No Sound Playing
1. Check if sound file exists:
   ```bash
   ls /System/Library/Sounds/Glass.aiff
   ```
2. Test sound manually:
   ```bash
   afplay /System/Library/Sounds/Glass.aiff
   ```
3. Check system volume and audio settings

### Too Many Sounds
- Disable specific hooks by commenting out the `afplay` line
- Use quieter sounds like "Tink" instead of "Sosumi"
- Reduce volume with `-v` parameter

### Performance Impact
Sounds run in background (`&`) so they don't block hook execution. The `2>/dev/null` suppresses error messages if audio isn't available.

## Creating Your Sound Experience

Design your perfect audio feedback by:

1. **Testing different sounds** for each hook type
2. **Setting volumes** appropriate for your environment  
3. **Choosing contextual sounds** that match the action
4. **Balancing feedback** - not too overwhelming, but informative

Your Claude Code environment now provides rich audio feedback that enhances your coding workflow! 🎵