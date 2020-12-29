var http = require('http');
const { spawn, exec } = require('child_process');
const express = require('express');
const app = express();
app.use(require('cors')());

app.get('/', (req, res, next) => {
    res.json({message: "hello!"});
})

app.get('/cam1', (req, res, next) => {
    console.log("cam1");
    exec("/usr/bin/fswebcam -r 1280x720 -d /dev/video0 --png 9 /home/pi/water-flow-sensor/website/cameras/cam1.png", (err, stdout, stderr) => {
        if (err) {
            console.log(`error: ${err.message}`)
            return res.json({message: err});
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`)
            return res.json({message: stderr});
        }
        console.log(`stdout: ${stdout}`)
        return res.json({message: stdout});
    })
})

app.get('/cam2', (req, res, next) => {
    console.log('cam2');
    exec("/usr/bin/fswebcam -r 1280x720 -d /dev/video2 --png 9 /home/pi/water-flow-sensor/website/cameras/cam2.png", (err, stdout, stderr) => {
        if (err) {
            console.log(`error: ${err.message}`)
            return res.json({message: err});
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`)
            return res.json({message: stderr});
        }
        console.log(`stdout: ${stdout}`)
        return res.json({message: stdout});
    })
})

var server = http.createServer(app);
server.listen(3030);
console.log('server running on port 3030')