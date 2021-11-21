// set variables
const ctx = [
    document.getElementById("chart1"),
    document.getElementById("chart2"),
    document.getElementById("chart3")
];

const tables = [
    document.getElementById("table1"),
]

const data = [
    $('#Data').data('side_effect_status'),
    $('#Data').data('side_effect_status'),
    $('#Data').data('side_effect_status')
]

const config = [
    create_chart(tables[0], data[0], 'pie', 'x'),
    create_chart(null, data[2], 'bar', 'y'),
    create_chart(null, data[2], 'bar', 'y'),
]

const chart = [
    new Chart(ctx[0], config[0]),
    new Chart(ctx[1], config[1]),
    new Chart(ctx[2], config[2]),
];