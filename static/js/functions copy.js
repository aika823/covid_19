function change(e, i) {
    let parent = e.target.parentElement;
    while (parent.tagName.toLowerCase() !== "table") {
        parent = parent.parentElement;
    }
    const inputs = [...parent.getElementsByTagName("input")];
    console.log(inputs)
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
        add(i, index);
    } else {
        remove(i, index);
    }
}

function remove(index, parent) {
    console.log('remove')
    if (index === -1) {
        data.forEach((_val, i) => (data[i].isShow = false));
    } else data[index].isShow = false;
    update(parent);
}

function add(index, parent) {
    console.log('add')
    if (index === -1) {
        data.forEach((_val, i) => (data[i].isShow = true));
    } else data[index].isShow = true;
    update(parent);
}

function update(index) {
    console.log('update')
    chart[index].config.data = {
        labels: data.filter((val) => val.isShow).map((val) => val.label),
        datasets: [{
            label: "응답수",
            data: data.filter((val) => val.isShow).map((val) => val.value),
            backgroundColor: data
                .filter((val) => val.isShow)
                .map((val) => val.color),
            display: false,
        }, ],
    };
    chart[index].update();
}

function create_chart(table = null, data, chart_type, index_axis) {

    if (table) {
        data.forEach((val, i) => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td><input type="checkbox" onchange="change(event, ${i})"checked></td>
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