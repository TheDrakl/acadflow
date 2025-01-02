export function validateForm (form) {
    let isValid = true;
    Object.keys(form).forEach(key => {
        if (form[key].value === '') {
            form[key].error = 'This field is required';
            isValid = false;
        } else {
            form[key].error = '';
        }
    });
    return isValid;
}