
window.onload = () => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/user/getusername', false);
    httpRequest.send();
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const username = response['username'];
    if (username === 0) {
        window.location.href = "/home/";
    }
    
}