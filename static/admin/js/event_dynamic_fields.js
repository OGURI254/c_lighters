function addField() {
    // Create new field container
    const fieldContainer = document.createElement('div');
    fieldContainer.classList.add('field-container');

    // Create input for field name
    const fieldNameInput = document.createElement('input');
    fieldNameInput.setAttribute('type', 'text');
    fieldNameInput.setAttribute('name', 'field_name[]');
    fieldNameInput.setAttribute('placeholder', 'Field Name');
    fieldContainer.appendChild(fieldNameInput);

    // Create dropdown for field type
    const fieldTypeSelect = document.createElement('select');
    fieldTypeSelect.setAttribute('name', 'field_type[]');
    const types = ['Text', 'Number', 'Date', 'Time'];
    types.forEach(type => {
        const option = document.createElement('option');
        option.value = type.toLowerCase();
        option.textContent = type;
        fieldTypeSelect.appendChild(option);
    });
    fieldContainer.appendChild(fieldTypeSelect);

    // Create checkbox for required field
    const requiredCheckbox = document.createElement('input');
    requiredCheckbox.setAttribute('type', 'checkbox');
    requiredCheckbox.setAttribute('name', 'field_required[]');
    fieldContainer.appendChild(requiredCheckbox);

    // Append the new field container to the form
    document.getElementById('dynamic-fields').appendChild(fieldContainer);
}
