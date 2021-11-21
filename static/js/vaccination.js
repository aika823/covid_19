// set variables
const ctx = [
    document.getElementById("chart1"),
    document.getElementById("chart2"),
    document.getElementById("chart3"),
    document.getElementById("chart4"),
    document.getElementById("chart5"),
];
const tables = [
    document.getElementById("table1"),
    document.getElementById("table2"),
    document.getElementById("table3"),
    document.getElementById("table4"),
    document.getElementById("table5"),
];

const data = [
    $('#Data').data('vaccine_list_times'),
    $('#Data').data('vaccine_list_gender'),
    $('#Data').data('vaccine_list_age'),
    $('#Data').data('vaccine_list_underlying'),
    $('#Data').data('vaccine_list_type'),
]

// create chart
const config = [
    create_chart(tables[0], data[0], 0, 'bar', 'x'),
    create_chart(tables[1], data[1], 1, 'bar', 'x'),
    create_chart(tables[2], data[2], 2, 'bar', 'x'),
    create_chart(tables[3], data[3], 3, 'bar', 'x'),
    create_chart(tables[4], data[4], 4, 'bar', 'x'),
]
const chart = [
    new Chart(ctx[0], config[0]),
    new Chart(ctx[1], config[1]),
    new Chart(ctx[2], config[2]),
    new Chart(ctx[3], config[3]),
    new Chart(ctx[4], config[4])
];