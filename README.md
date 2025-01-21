# Browser Session Recorder & Replayer
This project is a tool that allows you to record and replay browser sessions. It uses [rrweb](https://github.com/rrweb-io/rrweb) for recording sessions, and [rrweb-player](https://github.com/rrweb-io/rrweb-player) for replaying them.

## Setup
1. Create a Python virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Record a session
1. Run the recorder client:
```bash
python record.py
```

2. Navigate to a website in your browser.

3. Click the extensions button in the top right corner of the browser and open `rrweb` extension.

4. Click the record button in the extension to start recording.

## Download a session
1. Click on the extension button in the browser.
2. Click on the button on the left on the top of the extension box.
3. Select the session you want to download.
4. Click on the download button.

## Replay a session
1. Put the session json file in the `public/sessions` directory.

2. Rename the file to `session.js` and convert it to a js file by adding `const session = ` at the beginning of the file.

3. Run the replay server:
```bash
python replay.py
```
4. Navigate to `http://localhost:8000` in your browser.

You can click on "Open in new tab" to snapshot the current page and open it in a new tab to be inspected more easily. This will save the current html of the iframe in the `snapshots` directory. Note that this will not preserve the values of the inputs. Do not click on link or buttons in the new tab as they will send real requests.

Note that using the playback slider might be buggy. Refresh the page to reset the playback.

## Compiling Recorder for Windows
```bash
pip install pyinstaller
pyinstaller record.spec
```
