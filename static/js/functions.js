function change(e, i, data_index) {
    console.log(data[0]);
    let parent = e.target.parentElement;
    while (parent.tagName.toLowerCase() !== "table") {
        parent = parent.parentElement;
    }
    const inputs = [...parent.getElementsByTagName("input")];
    if (i === -1) {
        if (e.target.checked) {
            console.log("체크된 놈을 클릭");
            [...parent.getElementsByTagName("input")].forEach(
                (dom) => (dom.checked = true)
            );
        } else {
            console.log("체크 안된 놈을 클릭");
            [...parent.getElementsByTagName("input")].forEach(
                (dom) => (dom.checked = false)
            );
        }
    }
    if (
        inputs
        .slice(1)
        .map((dom) => dom.checked)
        .reduce((prev, cur) => prev && cur)
    ) {
        inputs[0].checked = true;
    } else {
        inputs[0].checked = false;
    }
    const id = parent.getAttribute("id");
    const index = Number(id.charAt(id.length - 1)) - 1;
    if (e.target.checked) {
        add(i, index, data_index);
    } else {
        remove(i, index, data_index);
    }
}

function remove(index, parent, data_index) {
    var new_data = data[data_index];
    console.log(new_data);
    console.log('remove')
    if (index === -1) {
        new_data.forEach((_val, i) => (new_data[i].isShow = false));
    } else new_data[index].isShow = false;
    update(parent, data_index);
}

function add(index, parent, data_index) {
    var new_data = data[data_index];
    console.log(new_data);
    if (index === -1) {
        new_data.forEach((_val, i) => (new_data[i].isShow = true));
    } else new_data[index].isShow = true;
    update(parent, data_index);
}

function update(index, data_index) {
    console.log('update')
    chart[index].config.data = {
        labels: data[data_index].filter((val) => val.isShow).map((val) => val.label),
        datasets: [{
            label: "응답수",
            data: data[data_index].filter((val) => val.isShow).map((val) => val.value),
            backgroundColor: data[data_index]
                .filter((val) => val.isShow)
                .map((val) => val.color),
            display: false,
        }, ],
    };
    chart[index].update();
}

function create_chart(table = null, data, index, chart_type, index_axis) {
    if (table) {
        data.forEach((val, i) => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td><input type="checkbox" onchange="change(event, ${i}, ${index})"checked></td>
                <td>${val.label}</td>
                <td style="text-align: right;">${val.value}</td>
                <td width="8%">${val.percentage}%</td>
            `;
            table.appendChild(tr);
        });
    }
    const result = {
        type: chart_type,
        data: {
            labels: data.filter((val) => val.isShow).map((val) => val.label),
            datasets: [{
                label: "응답수",
                data: data.filter((val) => val.isShow).map((val) => val.value),
                backgroundColor: data
                    .filter((val) => val.isShow)
                    .map((val) => val.color),
                display: false,
            }, ],
        },
        options: {
            indexAxis: index_axis,
            plugins: {
                legend: {
                    display: false,
                },
            },
        },
    };

    return result;
}