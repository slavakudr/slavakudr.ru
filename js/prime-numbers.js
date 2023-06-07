let maxNum = prompt('Вывод простых чисел до указанного числа', '');
let result = '';

next:
for (oneNum = 2; oneNum < maxNum; oneNum++) {

    for (twoNum = 2; twoNum < oneNum; twoNum++) {
        if (oneNum % twoNum == 0) {
            continue next;
        }
    }


    result = result + oneNum + ' ';
}

document.getElementById('output').innerHTML = result;