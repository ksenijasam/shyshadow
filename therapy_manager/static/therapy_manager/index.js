var appointmentDateInput = document.getElementById("appointment_date");
var requiredDateText = document.getElementById("date_required");
var newAppointment = document.getElementById("new_appointment");
var appointmentDetailsModal = document.getElementById("appointmentDetailsModal");
var closeModal = document.getElementById("closeModal");
var appointmentDetails = document.getElementById("appointmentDetails");
var cancelAlert = document.getElementById("cancelAlert");
var requiredDiaryDateText = document.getElementById("diary_date_required");
var diaryEntryDateInput = document.getElementById("diary_entry_date");
var diaryEntry = document.getElementById("diary_entry");
var diaryEntryTitle = document.getElementById("diary_entry_title");
var diaryEntryButton = document.getElementById("entry_button");


document.addEventListener('DOMContentLoaded', function () {
    requiredDateText ? requiredDateText.style.display = 'none' : null;
    newAppointment ? newAppointment.style.display = 'none' : null;
    cancelAlert ? cancelAlert.style.display = 'none' : null;
    requiredDiaryDateText ? requiredDiaryDateText.style.display = 'none' : null;
    diaryEntry ? diaryEntry.style.display = 'none' : null;
    diaryEntryTitle ? diaryEntryTitle.style.display = 'none' : null;
    diaryEntryButton ? diaryEntryButton.style.display = 'block' : null;
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

var appointmentID = null;

function viewAppointment(id, client, date, title, comment, status) {

    if(status === 'canceled') {
        cancelAlert.style.display = 'block';

        return;
    };

    appointmentID = id;

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
            <div class="col-3">
                <button class="btn btn-danger" type="submit" onclick="cnacelCanceling()"> Cancel</button>
            </div>
            <div class="col-3">
                <button class="btn btn-info" type="button" onclick="cnacelCanceling()"> Dismiss</button>
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

    try {
        const csrftoken = getCookie('csrftoken');
        const headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        };

        fetch('/appointments/' + appointmentID, {
            method: 'POST',
            headers: headers
        }) 
        .then((response) => response.json())
        .then(response => {
            if(response.message === 'Successfully canceled appointment') {
                window.location.reload();
            };
        });
    }
    catch {
        alert('Error occured, please try again.');
    }
};

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

cancelAlert.addEventListener('click', () => {
    cancelAlert.style.display = 'none';
});

function addDiaryEntry() {

    if (!diaryEntryDateInput.value) {
        requiredDiaryDateText.style.display = 'block';

        return;
    };

    diaryEntry.style.display = 'block';
    diaryEntryTitle.style.display = 'block';
    diaryEntryButton.style.display = 'none';
    
};

function dateDiaryEntryClicked() {
    requiredDiaryDateText.style.display = 'none';
};