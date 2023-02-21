const { app, BrowserWindow } = require('electron')
const path = require('path')
const prepareRenderer = require('electron-next')

function createWindow () {
  const win = new BrowserWindow({
    width: 1200,
    height: 960,
  })

  win.loadURL('http://localhost:3000/')
}

app.whenReady().then(() => {
  createWindow()
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
