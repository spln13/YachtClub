window.onload = () => {
    const btn = document.querySelector('#btn')
    const index = document.getElementById('yacht')
    btn.addEventListener('click', function (e) {
        e.preventDefault();
        const idx = index.selectedIndex;
        console.log(idx);
        // 1: TATIANA, 2: SNOW, 3: STARBURST
        let yacht_map = {
            1: "TATIANA",
            2: "SNOW",
            3: "STARBURST"
        }
        const httpRequest = new XMLHttpRequest();
        const dataToSend = {"yachtname": yacht_map[idx]}
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