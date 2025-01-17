function snapshot() {
    const contentDocument = document.querySelector(".replayer-wrapper > iframe").contentDocument;
    fetch('http://localhost:8000/snapshot', {
        method: 'POST',
        body: new XMLSerializer().serializeToString(contentDocument),
    }).then(response => response.json()).then(data => {
        console.log(data);
        window.open(`http://localhost:8000/snapshots/${data.filename}`, '_blank');
    });
}

const rrwp = new rrwebPlayer({
    target: document.body, // customizable root element
    props: {
      events: session.events,
    },
});

document.body.appendChild(rrwp);