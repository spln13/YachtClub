const logout = () => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/login/userlogout', false);
    httpRequest.send();
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const code = response['code'];
    if (code === 1) {
        alert('登出成功');
        window.location.href = '/home/'
    } else {
        alert('登出失败');
    }
}

window.onload = () => {
    const httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/user/getusername', false);
    httpRequest.send();
    const strReceive = String(httpRequest.response);
    const response = JSON.parse(JSON.parse(strReceive));
    const username = response['username'];  // 0: 未登录; username: 用户名
    console.log(username)
    if (username !== 0) { // 登陆状态 修改右上角
        let right = document.getElementById("right");
        console.log(right);
        right.innerHTML = '<li>' + username +'</li><button type="button" onclick="logout()" class="btn btn-warning">登出</button>'
    }
    const btn = document.querySelector('#btn')
    const index = document.getElementById('yacht')
    btn.addEventListener('click', function (e) {
        e.preventDefault();
        const idx = index.selectedIndex;
        if (idx === 0) {
            alert('请选择游艇');
            return null;
        }
        console.log(idx);
        // 1: TATIANA, 2: SNOW, 3: STARBURST
        let yacht_map = {
            1: "TATIANA",
            2: "SNOW",
            3: "STARBURST",
            4: "ELADE",
            5: "TIMELESS",
            6: "DUSUR",
            7: "RL NOLOR",
            8: "GIAO-LU"
        }
        const httpRequest = new XMLHttpRequest();
        const dataToSend = {"yachtname": yacht_map[idx]}
        // console.log(dataToSend);
        httpRequest.open('POST', '/api/lease/lease', false);
        httpRequest.send(JSON.stringify(dataToSend));
        const strReceive = String(httpRequest.response);
        const response = JSON.parse(JSON.parse(strReceive));
        const code = response['code'];
        if (code === 0) {
            alert('租赁成功');
        }
        else if (code === 2) {
            alert('无剩余船只');
        }
        else {
            alert('租赁失败');
        }
    })
}