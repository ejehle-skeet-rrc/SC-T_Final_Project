const form = document.getElementById("burgerCustomizationForm");

form.addEventListener("submit", (event) =>{
    debugger;
    const errorMessages = document.querySelectorAll(".error-message");
    for (const el of errorMessages){
        el.remove();
    }

    event.preventDefault();

    if(validateForm()){
        form.submit();
        console.log("Success");
    } else {
        console.log("Failed");
    }
})

const showInputError = (inputElement, message) => {
    debugger;
    const errorDisplay = document.createElement("span");
    errorDisplay.innerText = message;
    errorDisplay.className = "error-message";
    errorDisplay.setAttribute("role", "alert");

    inputElement.parentElement.appendChild(errorDisplay);
}

const validateForm = () =>{
    debugger;
    let isValid = true;
    // First Section Validations
    // Bread Dropdown Menu Check
    const breadType = document.getElementById("bread");
    if (isSelected(breadType) === false){
        isValid = false;
    }

    // Burger Amount Check
    const amountInput = document.getElementById("total");
    if (isNotZeroOrLower(amountInput) === false){
        isValid = false;
    }

    // Second Section Validations
    // Sides Dropdown Menu
    const sidesChoice = document.getElementById("sides");
    if (isSelected(sidesChoice) === false){
        isValid = false;
    }

    // Third Section Validations
    // Name Field Check (One for Alphabetical, One for Blank)
    const nameInput = document.getElementById("name");
    if (isNotEmpty(nameInput) === false){
        isValid = false;
    }

    // Email Address Check
    const emailInput = document.getElementById("receiptEmail");
    if (isValidEmail(emailInput) === false) {
        isValid = false;
    }
    return isValid;
}

// Functions for Validation
const isNotZeroOrLower = (numberField) => {
    if (numberField.value <= 0){
        showInputError(numberField, "Amount must be higher than zero!");
        return false;
    }
}

const isSelected = (dropdownField) => {
    if (dropdownField.value === "dummy"){
        showInputError(dropdownField, "Must choose an option below!");
        return false;
    } else if (dropdownField.value === ""){
        showInputError(dropdownField, "Must choose an option below!");
        return false;
    }
}

const isNotEmpty = (textField) => {
    if (textField.value === ""){
        showInputError(textField, "Name cannot be blank!");
        return false;
    }
}

const isValidEmail = (emailField) => {
    const complexEmailPattern = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;
    if (!complexEmailPattern.test(emailField.value)) {
        showInputError(emailField, "Email is not valid!");
        return false;
    }
}