document.addEventListener("DOMContentLoaded", () => {
    console.log("JS loaded");

    const deptSelect   = document.getElementById("id_department");
    const doctorSelect = document.getElementById("id_doctor");
    const dateSelect   = document.getElementById("date");
    const slotSelect   = document.getElementById("id_timeslot");

    // Attach metadata to timeslot options

    // Hide all doctors & timeslots initially
    [...doctorSelect.options].forEach(o => { if (o.value) o.hidden = true });
    [...slotSelect.options].forEach(o => { if (o.value) o.hidden = true });

    // FILTER DOCTORS BY DEPARTMENT
    deptSelect.addEventListener("change", () => {
        let dept = deptSelect.value;

        // Reset doctor dropdown
        doctorSelect.value = "";
        [...doctorSelect.options].forEach(option => {
            if (!option.value) return;

            let docDept = option.dataset.dept;
            option.hidden = !(docDept === dept);
        });

        // Reset timeslots
        slotSelect.value = "";
        filterSlots();
    });

    // FILTER TIMESLOTS BY DOCTOR + DATE
    doctorSelect.addEventListener("change", filterSlots);
    dateSelect.addEventListener("change", filterSlots);

    function filterSlots() {
        let selectedDoctor = doctorSelect.value;
        let selectedDate   = dateSelect.value;
        console.log("doctor:", selectedDoctor, "date:", selectedDate);

        [...slotSelect.options].forEach(option => {
            if (!option.value) return;

            let doc    = option.dataset.doctor;
            let date   = option.dataset.date;
            let booked = option.dataset.booked === "True";
            console.log("option", option.value, "doc:", doc, "date:", date, "booked:", booked);

            option.hidden = !(doc == selectedDoctor &&
                              date === selectedDate &&
                              !booked);
        });
    }
});