var appointmentDateInput = document.getElementById("appointment_date");
var requiredDateText = document.getElementById("date_required");
var newAppointment = document.getElementById("new_appointment");
var appointmentDetailsModal = document.getElementById("appointmentDetailsModal");
var closeModal = document.getElementById("closeModal");
var appointmentDetails = document.getElementById("appointmentDetails");

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
    appointmentDetails.innerHTML = `
    <h1>${title}</h1>
    <div>
        <p>Appointment date: ${date}</p>
        <p>${comment}</p>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="isMeetingCanceled" onclick="cancelationReason()">
            <label class="form-check-label" for="isMeetingCanceled" onclick="cancelationReason()">
                Cancel meeting ?
            </label>
        </div>
        <div class="row" id="cancelComment" style="display: none;">
            <div class="col-6">
                <div class="form-group">
                    <label for="comment">Would you like to leave cnacelation reason ?</label>
                    <textarea class="form-control" name="cancelComment" id="cancelComment" rows="3"></textarea>
                </div>
            </div>
            <div class="col-6">
                <button class="btn btn-danger" type="button" onclick="cnacelCanceling()"> Cancel</button>
            </div>
        </div>
    </div>`
};

closeModal.onclick = function() {
    appointmentDetailsModal.style.display = "none";
};

window.onclick = function(event) {
    if (event.target == appointmentDetailsModal) {
        appointmentDetailsModal.style.display = "none";
    };
};


function cancelationReason() {
    var cancelComment = document.getElementById("cancelComment");

    if (isMeetingCanceled.checked) {
        cancelComment.style.display = "block";
    } else {
        cancelComment.style.display = "none";
    }
};

function cnacelCanceling() {
    document.getElementById("cancelComment").style.display = "none";
    isMeetingCanceled.checked = false;
}