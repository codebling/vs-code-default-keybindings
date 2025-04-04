Keybindings for VS Code

- [Why](#why)
- [Example](#example)
- [How to use these files](#how-to-use-these-files)
- [Unmapping](#unmapping)
- [VS Code Extension](#vs-code-extension)
- [Contributors](#contributors)

# Why

Code uses key combinations that are idiomatic to each platform. "Find" might be bound to F3 on Windows, but Command-F on Mac. This can be supremely annoying if you use Code on multiple operating systems, in which case it's preferable to use keyboard shortcuts that feel the same on each OS. 

This repo keeps an up-to-date dump of key bindings for Code on each operating system, which can be used to apply default keys for another OS, or remove Code's default keys entirely. 

# Example

Situation: you are used to working on Windows but you are currently on a Mac. You notice Ctrl+Z doesn't work, because on a Mac the default binding is Cmd+Z, which is annoying because it breaks your muscle memory, interrupting your flow state. You open the keybindings file and paste macos.negative.keybindings.json. This removes the default Mac keybindings. Then you paste windows.keybindings.json. This adds default Windows keybindings. Ctrl+Z now works.

# How to use these files

Press `F1` or `Ctrl Shift P` or `Cmd Shift P` to open the "Show All Commands" search box, then search for "keyboard" and choose "Preferences: Open Keyboard Shortcuts (JSON)". This will open a new editor file containing the custom key combinations you've already configured - be sure not to overwrite these. Paste in the contents of the file you want - that's it! For example, if you're on Linux but want to use Mac keys, paste the contents of `macos.keybindings.json` into your editor. 

# Unmapping

The `.negative.keybindings.json` are "opposite" mappings - they remove keyboard shortcuts for a given OS. These will return VS Code to a blank slate, with no keyboard shortcuts at all, so it generally only makes sense to use these in conjunction with another keybinding file. 

One would typically only use these if you found yourself accidentally triggering certain actions - you may be pressing keys which normally do nothing in VS Code on another OS. 

For example, if you're used to working on Windows but are currently on Mac, you can apply `macos.negative.keybindings.json` (as described in [How to use these files](#how-to-use-these-files)) to remove all the Mac shortcuts. Then, at the bottom of the Code keybindings.json editor, delete the bottom `]`, add a comma `,`, then paste the contents of `windows.keybindings.json`. Remove the top `[` from the pasted contents. If you've done this correctly, there should only be one set of `[` and `]` at the top level and VS Code should not complain when the file is saved. 

# VS Code Extension

[jbro](https://github.com/jbro/vscode-default-keybindings) has developed [an extension](https://marketplace.visualstudio.com/items?itemName=jbro.vscode-default-keybindings) (or [link to Open VSX Registroy](https://open-vsx.org/extension/jbro/vscode-default-keybindings) for those using open source versions of VS Code) to facilitate applying these settings. Install the extension, then installing the and removing keymaps for other operatings systems is as easy as changing a few settings. Have a look at the extension documentation for more details.

# Contributors

This project was made possible by the following contributors:
* [moltenform](https://github.com/moltenform), who created the Python scripts to treat the files
* [tshino](https://github.com/tshino), who was able to automate the process of retrieving new shortcuts from VS Code and package it in GitHub Actions
* [zimtsui](https://github.com/zimtsui), [blackwindforce](https://github.com/blackwindforce), and others, who contributed updates to the binding files before the process was automated. 