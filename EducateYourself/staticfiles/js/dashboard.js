document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      events: [
        // Example events (replace with your actual events)
        {
          title: 'Class Schedule',
          start: '2024-02-01T10:00:00',
          end: '2024-02-01T12:00:00'
        },
        {
          title: 'Assignment Deadline',
          start: '2024-02-05',
          allDay: true
        },
        // Add more events as needed
      ]
    });

    calendar.render();
  });