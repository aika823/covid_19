// 접종현황 시작
const ctx = [
    document.getElementById("chart1"),
    document.getElementById("chart2"),
    document.getElementById("chart3")
];

const tables = [
    document.getElementById("table2"),
]

const data = [
    {
        label: "모더나",
        value: 160,
        color: "#D1B2FF",
        isShow: true
    },
    {
        label: "화이자",
        value: 238,
        color: "#B2CCFF",
        isShow: true
    },
    {
        label: "아스트라제네카",
        value: 38,
        color: "#B2EBF4",
        isShow: true
    },
    {
        label: "얀센",
        value: 11,
        color: "#CEF279",
        isShow: true
    },
    {
        label: "기타",
        value: 3,
        color: "#FFE08C",
        isShow: true
    },
];

const data2 = [
    {
        label: "모더123나",
        value: 160,
        color: "#D1B2FF",
        isShow: true
    },
    {
        label: "화이123자",
        value: 238,
        color: "#B2CCFF",
        isShow: true
    },
    {
        label: "아스트123라제네카",
        value: 38,
        color: "#B2EBF4",
        isShow: true
    },
    {
        label: "얀123센",
        value: 11,
        color: "#CEF279",
        isShow: true
    },
    {
        label: "기123타",
        value: 3,
        color: "#FFE08C",
        isShow: true
    },
];

const data3 = [
    {
        label: "123모더나",
        value: 160,
        color: "#D1B2FF",
        isShow: true
    },
    {
        label: "123화이123자",
        value: 238,
        color: "#B2CCFF",
        isShow: true
    },
    {
        label: "123아스트123라제네카",
        value: 38,
        color: "#B2EBF4",
        isShow: true
    },
    {
        label: "123얀123센",
        value: 11,
        color: "#CEF279",
        isShow: true
    },
    {
        label: "123기123타",
        value: 3,
        color: "#FFE08C",
        isShow: true
    },
];

const datas = [
    data,
    data2,
    data3
]

tables.forEach((dom, index) => {
    datas[index].forEach((val, i) => {
        const tr = document.createElement("tr")
        tr.innerHTML = `
            <td><input type="checkbox" onchange="onChange(event, ${i})"></td>
            <td>${val.label}</td>
            <td style="text-align: right;">${val.value}</td>
            <td width="8%">${Math.round(Math.random() * 99) + 1}%</td>
        `;
        dom.appendChild(tr)
    })
})

function createConfig(index) {
    return {
        type: "pie",
        data: {
            labels: datas[index].filter(val => val.isShow).map(val => val.label),
            datasets: [
                {
                    label: "응답수",
                    data: datas[index].filter(val => val.isShow).map(val => val.value),
                    backgroundColor: datas[index].filter(val => val.isShow).map(val => val.color),
                    display: false
                }
            ],
        },
        options: {
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    }
}

const chart = [
    new Chart(ctx[0], {...createConfig(0), type: "bar", options: {
        indexAxis: "y",
        plugins: {
            legend: {
                display: false
            }
        }
    }}),
    new Chart(ctx[1], createConfig(1)),
    new Chart(ctx[2], {...createConfig(2), type: "bar", options: {
        indexAxis: "y",
        plugins: {
            legend: {
                display: false
            }
        }
    }}),
];

function onChange(e, i) {
    let parent = e.target.parentElement;
    while(parent.tagName.toLowerCase() !== "table") parent = parent.parentElement;
    const inputs = [...parent.getElementsByTagName("input")];
    if(i === -1) {
        if(e.target.checked) [...parent.getElementsByTagName("input")].forEach(dom => dom.checked = true);
        else [...parent.getElementsByTagName("input")].forEach(dom => dom.checked = false);
    }
    if(inputs.slice(1).map(dom => dom.checked).reduce((prev, cur) => prev && cur)) inputs[0].checked = true;
    else inputs[0].checked = false;
    const id = parent.getAttribute("id");
    const index = Number(id.charAt(id.length - 1)) - 1;
    if(e.target.checked) remove(i, index);
    else add(i, index)
}

function remove(index, parent) {
    if(index === -1) {
        datas[parent].forEach((_val, i) => datas[parent][i].isShow = false);
    } else datas[parent][index].isShow = false;

    update(parent);
}

function add(index, parent) {
    if(index === -1) {
        datas[parent].forEach((_val, i) => datas[parent][i].isShow = true);
    } else datas[parent][index].isShow = true;

    update(parent);
}

function update(index) {
    console.log(datas[index])
    chart[index].config.data = {
        labels: datas[index].filter(val => val.isShow).map(val => val.label),
        datasets: [
            {
                label: "응답수",
                data: datas[index].filter(val => val.isShow).map(val => val.value),
                backgroundColor: datas[index].filter(val => val.isShow).map(val => val.color),
                display: false
            }
        ],
    }
    
    chart[index].update();
}
//접종현황 끝