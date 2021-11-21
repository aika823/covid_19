// set variables
const ctx = [
    document.getElementById("chart1")
];

const tables = [
    document.getElementById("table1")
];

const data = [
    $('#Data').data('vaccine_list'),
]

// get data
// vaccine_list = $('#Data').data('vaccine_list');
// vaccine_list.forEach(function(element) {
//     var obj = {};
//     obj['label'] = element.vaccine_name;
//     obj['value'] = element.count;
//     obj['color'] = "#D1B2FF";
//     obj['isShow'] = true;
//     obj['percentage'] = element.percentage;
//     data.push(obj)
// });

const config = [
    create_chart(tables[0], data[0], 'bar', 'x')
]

const chart = [
    new Chart(ctx[0], config[0])
];