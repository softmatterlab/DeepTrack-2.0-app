const net = require('net');

const port = process.env.PORT ? process.env.PORT - 100 : 3000;

process.env.ELECTRON_START_URL = `http://localhost:${port}`;

const client = new net.Socket();

const exec = require('child_process').exec;

// Start react server
exec('npm start');

let startedElectron = false;
const tryConnection = () => {
    console.log('Connecting...');
    client.connect({ port: port }, () => {
        client.end();
        if (!startedElectron) {
            startedElectron = true;
            exec('npm run electron');
        }
    });
};

tryConnection();

client.on('error', (e) => {
    console.error(e);
    setTimeout(tryConnection, 1000);
});