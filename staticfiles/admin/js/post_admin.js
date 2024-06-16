document.addEventListener('DOMContentLoaded', function() {
    var isScheduledCheckbox = document.getElementById('id_is_scheduled');
    var scheduledTimeField = document.getElementById('id_scheduled_time');
    var dateInput = document.getElementById('id_scheduled_time_0'); // Date input
    var timeInput = document.getElementById('id_scheduled_time_1'); // Time input
    var dateLink = scheduledTimeField.closest('.field-scheduled_time').querySelector('a[href^="#calendarlink"]'); // Date link
    var nowLink = scheduledTimeField.closest('.field-scheduled_time').querySelector('a[href^="#clocklink"]'); // Now link

    function toggleScheduledTimeField() {
        if (isScheduledCheckbox.checked) {
            dateInput.removeAttribute('disabled');
            timeInput.removeAttribute('disabled');
            if (dateLink) {
                dateLink.style.pointerEvents = 'auto';
                dateLink.style.color = '';
            }
            if (nowLink) {
                nowLink.style.pointerEvents = 'auto';
                nowLink.style.color = '';
            }
        } else {
            dateInput.setAttribute('disabled', 'disabled');
            timeInput.setAttribute('disabled', 'disabled');
            if (dateLink) {
                dateLink.style.pointerEvents = 'none';
                dateLink.style.color = 'grey';
            }
            if (nowLink) {
                nowLink.style.pointerEvents = 'none';
                nowLink.style.color = 'grey';
            }
        }
    }

    // 初期状態を設定
    toggleScheduledTimeField();

    // チェックボックスの状態が変わったときにフィールドの状態を更新
    isScheduledCheckbox.addEventListener('change', toggleScheduledTimeField);
});
