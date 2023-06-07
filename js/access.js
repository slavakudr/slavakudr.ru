let login = prompt('Ведите логин (верный admin)', '');
let password;

if (login === 'admin') {
    password = prompt('Введите пароль (верный 1234)', '');
    if (password === '1234') {
        alert('Добро пожаловать!');
    } else if (password === null) {
        alert('Отмена');
    } else {
        alert('Неверный пароль');
    }
} else if (login === null) {
    alert('Отмена');
} else {
    alert('Неверный логин');
}