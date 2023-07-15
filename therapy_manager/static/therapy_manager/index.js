var appointmentDateInput = document.getElementById("appointment_date");
var requiredDateText = document.getElementById("date_required");
var newAppointment = document.getElementById("new_appointment");
var appointmentDetailsModal = document.getElementById("appointmentDetailsModal");
var closeModal = document.getElementById("closeModal");

document.addEventListener('DOMContentLoaded', function() {
    requiredDateText.style.display = 'none';
    newAppointment.style.display = 'none';
});

function dateInputClicked() {
    requiredDateText.style.display = 'none';
    appointmentDateInput.style.border = 'initial';
};

function createNewAppointment() {
    appointmentDateInput.style.border = 'initial';

    if(!appointmentDateInput.value) {
        appointmentDateInput.style.border = '1px solid red';
        requiredDateText.style.display = 'block';
        requiredDateText.style.color = 'red';

        return;
    };

    newAppointment.style.display = 'block';
};

function viewAppointment(client, date, title,comment) {
    appointmentDetailsModal.style.display = "block";
    console.log(title);
};

closeModal.onclick = function() {
    appointmentDetailsModal.style.display = "none";
};

window.onclick = function(event) {
    if (event.target == appointmentDetailsModal) {
        appointmentDetailsModal.style.display = "none";
    };
};