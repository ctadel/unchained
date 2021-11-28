function genericTimeFormat(date){
      let ye = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(date);
      let mo = new Intl.DateTimeFormat('en', { month: 'short' }).format(date);
      let da = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(date);

      let minutes = date.getMinutes();
      let hour = date.getHours()%12;
      let ampm = hour >= 12 ? 'p.m.' : 'a.m.';

      date = (`${mo}. ${da}, ${ye}, ${hour}:${minutes} ${ampm}`);
      return date;
}

document.querySelector("#reload_btn").addEventListener('click',()=>{
    fetch('',
        {
            headers  : {
                'Accept' :'application/json',
                'Content-Type' : 'application/json',
                            },
            method  : 'POST',
        }
    )
      .then(response => response.json())
      .then(data => {
          data = JSON.parse(data);

          last_updated = genericTimeFormat(new Date(Date.parse(data.last_updated)))

          document.querySelector('#ip_address').innerHTML  = data.ip;
          document.querySelector('#ip_update_detail').innerHTML = 'Last Updated: ' + last_updated;
          console.log(data)
      });
});

