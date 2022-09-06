/*globals $:false */

// 选择班级的复选框的点击事件
function checkboxOnclick(checkbox, cls) {
    'use strict';
    if (checkbox.checked === true) {
        show_students(cls);
        // submitForm();
    } else {
        remove_students(cls);
        // submitForm();
    }
}

// 显示学生
function show_students(cls) {
    'use strict';
    const req = new XMLHttpRequest();  // 1 创建对象
    req.open('GET', 'http://127.0.0.1:5000/get_cla/' + cls + '/');  // 2 初始化
    req.send();  // 3 发送
    req.onreadystatechange = function () {  // 4 时间绑定
        if (req.readyState === 4 && this.status === 200) {
            const res = JSON.parse(req.response);  // 将字符串类型转为json类型
            const students = res.stu;
            //获取标签名字为tbody的第一个标签，并将其赋值给tbody
            const tbody = document.getElementsByTagName('tbody')[0];
            for (let i = 0; i < students.length; i++) {
                const name = students[i];
                const newTr = tbody.firstElementChild.cloneNode(true); // 产生一个tr
                newTr.removeAttribute('style');
                newTr.children[1].innerHTML = cls;  // 第一个表格中填班级
                newTr.children[2].innerHTML = name;  // 第二个表格中填学生姓名
                newTr.children[3].children[0].children[0].setAttribute('name', 'user-' + cls + '-' + name);  // 设置select标签的name属性
                tbody.appendChild(newTr);
            }
        }
    };
}

// 移除学生
function remove_students(cls) {
    'use strict';
    const table = document.getElementsByTagName('tbody')[0];
    const rows = table.rows;
    const len = rows.length;
    for (let i = len - 1; i >= 1; i--) {
        const now_row = rows[i];
        const cells = now_row.cells;
        const table_cls = cells[1].firstChild.nodeValue;  // 班级
        // const table_student = cells[2].firstChild.nodeValue;  // 学生姓名
        if (cls === table_cls) {
            table.deleteRow(i);  // 移除行
        }
    }
}


// 移除学生
function read_students() {
    'use strict';
    const table = document.getElementsByTagName('tbody')[0];
    const rows = table.rows;
    const len = rows.length;
    const cls_list = []
    for (let i = len - 1; i >= 1; i--) {
        const now_row = rows[i];
        const cells = now_row.cells;
        const table_student = cells[2].firstChild.nodeValue;  // 学生姓名
        cls_list.push(table_student)
    }
    const req = new XMLHttpRequest();  // 1 创建对象
    req.open('GET', 'http://127.0.0.1:5000/get_nam/' + cls_list + '/');  // 2 初始化
    req.send();  // 3 发送
    req.onreadystatechange = function () {  // 4 时间绑定
        if (req.readyState === 4 && this.status === 200) {
            alert(req.response);  // 将字符串类型转为json类型
        }}

}

// 刷新请求
function submitForm() {
    const form = document.getElementById('myfrom');
    form.submit();
}

// function random() {
//     var arr = ['飞鸟博客', '飞鸟慕鱼博客', 'feiniaomy.com'];
//     var index = Math.floor((Math.random() * arr.length));
//     console.log(arr[index]);
// }