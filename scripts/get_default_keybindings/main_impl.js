'use strict';
const os = require('os');
const path = require('path');
const fsPromises = require('fs/promises');
const vscode = require('vscode');

const sleep = msec => new Promise(resolve => setTimeout(resolve, msec));

async function openDefaultKeybindingsFile() {
    return await new Promise((resolve, reject) => {
        const listener = vscode.window.onDidChangeVisibleTextEditors(textEditors => {
            for (const textEditor of textEditors) {
                const uri = textEditor.document.uri;
                if (uri.scheme === 'vscode' && path.basename(uri.path) === 'keybindings.json') {
                    listener.dispose();
                    resolve(textEditor.document);
                }
            }
        });
        vscode.commands.executeCommand('workbench.action.openDefaultKeybindingsFile').then(() => {
            setTimeout(() => {
                console.error('timeout');
                listener.dispose();
                reject();
            }, 10 * 1000);
        });
    });
}

function makeHeader(platform) {
    const target = (
        platform === 'win32' ? 'Windows' :
        platform === 'darwin' ? 'macOS' :
        'Linux'
    );
    const signature = `${vscode.env.appName} ${vscode.version} for ${target}`;
    const header = `// Default Keybindings of ${signature}\n`;
    return header;
}

function makeOutputFilePath(platform) {
    const prefix = (
        platform === 'win32' ? 'windows' :
        platform === 'darwin' ? 'macos' :
        'linux'
    );
    const outputPath = path.resolve(__dirname, `../${prefix}.keybindings.raw.json`);
    return outputPath;
}

async function run() {
    await sleep(2000);
    const document = await openDefaultKeybindingsFile();
    const json = document.getText();
    const platform = os.platform();
    const header = makeHeader(platform);
    const outputPath = makeOutputFilePath(platform);
    await fsPromises.writeFile(outputPath, header + json);
    console.log(`The default keybindings JSON has been successfully saved to ${outputPath}.`);
}

module.exports = {
    run
};
