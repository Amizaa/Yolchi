document.getElementById('sidebar-toggle').addEventListener('click', function() {
    var sidebar = document.getElementById('sidebarMenu');
    sidebar.classList.toggle('collapse');
});


document.getElementById('toggle-report').addEventListener('click', function() {
    var report = document.getElementById('report');
    report.classList.toggle('collapse');
});
