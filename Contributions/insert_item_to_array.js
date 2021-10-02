function insertElement() {
    let array = [1, 2, 3, 4];

    let index = 3;

    let element = 8;
  
    for (let i = array.length; i > index; i--) {

        array[i] = array[i-1];
    }

    array[index] = element;

    console.log(array);
}

insertElement();
