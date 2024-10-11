const isLeapYear = (year) => {
  return (
    (year % 4 === 0 && year % 100 !== 0 && year % 400 !== 0) ||
    (year % 100 === 0 && year % 400 === 0)
  );
};
const getFebDays = (year) => {
  return isLeapYear(year) ? 29 : 28;
};
let calendar = document.querySelector('.calendar');
const month_names = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
  ];
let month_picker = document.querySelector('#month-picker');
const dayTextFormate = document.querySelector('.day-text-formate');
const timeFormate = document.querySelector('.time-formate');
const dateFormate = document.querySelector('.date-formate');

month_picker.onclick = () => {
  month_list.classList.remove('hideonce');
  month_list.classList.remove('hide');
  month_list.classList.add('show');
  dayTextFormate.classList.remove('showtime');
  dayTextFormate.classList.add('hidetime');
  timeFormate.classList.remove('showtime');
  timeFormate.classList.add('hideTime');
  dateFormate.classList.remove('showtime');
  dateFormate.classList.add('hideTime');
};

const generateCalendar = (month, year) => {
  let calendar_days = document.querySelector('.calendar-days');
  calendar_days.innerHTML = '';
  let calendar_header_year = document.querySelector('#year');
  let days_of_month = [
      31,
      getFebDays(year),
      31,
      30,
      31,
      30,
      31,
      31,
      30,
      31,
      30,
      31,
    ];

  let currentDate = new Date();

  month_picker.innerHTML = month_names[month];

  calendar_header_year.innerHTML = year;

  let first_day = new Date(year, month);


  for (let i = 0; i <= days_of_month[month] + first_day.getDay() - 1; i++) {

    let day = document.createElement('div');
    let dataSide = document.querySelector('.data-side');
    let text = dataSide.querySelector('.date');
    let opt1 = dataSide.querySelector('.option-1');
    let opt2 = dataSide.querySelector('.option-2');
    let avg1 = dataSide.querySelector('.avg-1');
    let avg2 = dataSide.querySelector('.avg-2');
    let per1 = dataSide.querySelector('.per-1');
    let per2 = dataSide.querySelector('.per-2');
    //let total1 = dataSide.querySelector('.total-1');
    //let total2 = dataSide.querySelector('.total-2');
    let noData = document.querySelector(".no-data-shown");
    let bar1=document.querySelector('.bar-chart')
    let loader = document.querySelector('#loader-wrapper');
    let data_text = document.querySelector('no-data-text');
    

    if (i >= first_day.getDay()) {
      let z = i - first_day.getDay() + 1;
      day.innerHTML = z;
      day.classList.add('d'+String(z));
      day.classList.add('day');

      if (i - first_day.getDay() + 1 === currentDate.getDate() &&
        year === currentDate.getFullYear() &&
        month === currentDate.getMonth()
      ) {
        day.classList.add('current-date');
      }
    }
    calendar_days.appendChild(day);
    if (i >= first_day.getDay()) {
        let d = i - first_day.getDay() + 1;
        let m = first_day.getMonth()+1;
        let y = first_day.getFullYear();
        const weekdayList = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
        let weekday = new Date(`${m} ${d} ${y}`);
        let wd = weekdayList[weekday.getDay()];
        

  
        document.querySelector('.d'+String(d)).addEventListener('click', function() {
            
            loader.style.display = 'inline-block';
            dataSide.style.display = 'flex';
            text.innerHTML=`${month_names[month]} ${d} ${y}`;
            console.log(`month: ${m}, day: ${d}, year: ${y}`);
        
            //implement weekend stuff
            dataSide.style.visibility = 'hidden'; 
            noData.style.display = 'flex';
            
        
            
            dataSide.style.visibility = 'visible';  
            noData.style.display = 'none';
            
            $.ajax({ 
              url: '/calendar_retrieval', 
              type: 'POST', 
              contentType: 'application/json', 
              data: JSON.stringify({ 'day': d, 'month' : m, 'year':y}), 
              success: function(response) {
                  let bool_school = response.no_school
                  if (bool_school == false){
              
                      //document.getElementById('output').innerHTML = response.result; 
                      console.log(`names: ${response.option_list}   
                                        avgs: ${response.avg_list}
                                        total_ratings: ${response.total_ratings}
                                        percenteages: ${response.percentages}
                                        `);

                      //put here
                      loader.style.display = 'none';
                      //checks which value is bigger, then assigns that index to the first
                      avg1.innerHTML = response.avg_list[0] >= response.avg_list[1] 
                                    ? response.avg_list[0] : response.avg_list[1];
                      avg2.innerHTML = response.avg_list[0] < response.avg_list[1] 
                                    ? response.avg_list[0] : response.avg_list[1];
                      opt1.innerHTML = response.avg_list[0] >= response.avg_list[1] 
                                    ? response.option_list[0] : response.option_list[1];
                      opt2.innerHTML = response.avg_list[0] < response.avg_list[1] 
                                    ? response.option_list[0] : response.option_list[1];
                      //total1.innerHTML = response.avg_list[0] >= response.avg_list[1] 
                      //              ? response.total_ratings[0] : response.total_ratings[1];
                      //total2.innerHTML = response.avg_list[0] < response.avg_list[1] 
                      //              ? response.total_ratings[0] : response.total_ratings[1];
                      per1.innerHTML = response.avg_list[0] >= response.avg_list[1] 
                                    ? response.percentages[0] : response.percentages[1];
                      per2.innerHTML = response.avg_list[0] < response.avg_list[1] 
                                    ? response.percentages[0] : response.percentages[1];
                      
                      //Plotly.react('external', data, {}); 
                  
            
            
                      fetch(`/bar_retrieval`, {
                        method: "POST",
                        credentials: "include",
                        body: JSON.stringify({ 'day': d, 'month' : m, 'year':y}),
                        cache: "no-cache",
                        headers: new Headers({
                          "content-type": "application/json"
                        })})
                      .then(resp => resp.ok && resp.json())
                      .then(data => {
                          if (!data) return;
                          console.log(data);
                          Plotly.react('external', data, {});
                    
                      });
                  } else {
                    loader.style.display = 'none';
                    dataSide.style.visibility = 'hidden'; 
                    noData.style.display = 'flex';
                    noData.textContent = 'No Menu Posted';
                  }

              }, 
              error: function(error) { 
                  console.log("error");
              } 
            });
          
          
            
        
            
        });
        
    }
  }
};

let month_list = calendar.querySelector('.month-list');
month_names.forEach((e, index) => {
  let month = document.createElement('div');
  month.innerHTML = `<div>${e}</div>`;

  month_list.append(month);
  month.onclick = () => {
    currentMonth.value = index;
    generateCalendar(currentMonth.value, currentYear.value);
    month_list.classList.replace('show', 'hide');
    dayTextFormate.classList.remove('hideTime');
    dayTextFormate.classList.add('showtime');
    timeFormate.classList.remove('hideTime');
    timeFormate.classList.add('showtime');
    dateFormate.classList.remove('hideTime');
    dateFormate.classList.add('showtime');
  };
});

(function() {
  month_list.classList.add('hideonce');
})();
document.querySelector('#pre-year').onclick = () => {
  --currentYear.value;
  generateCalendar(currentMonth.value, currentYear.value);
};
document.querySelector('#next-year').onclick = () => {
  ++currentYear.value;
  generateCalendar(currentMonth.value, currentYear.value);
};

let currentDate = new Date();
let currentMonth = { value: currentDate.getMonth() };
let currentYear = { value: currentDate.getFullYear() };
generateCalendar(currentMonth.value, currentYear.value);

const todayShowTime = document.querySelector('.time-formate');
const todayShowDate = document.querySelector('.date-formate');

const currshowDate = new Date();
const showCurrentDateOption = {
  year: 'numeric',
  month: 'long',
  day: 'numeric',
  weekday: 'long',
};
const currentDateFormate = new Intl.DateTimeFormat(
  'en-US',
  showCurrentDateOption
).format(currshowDate);
todayShowDate.textContent = currentDateFormate;
setInterval(() => {
  const timer = new Date();
  const option = {
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric',
  };
  const formateTimer = new Intl.DateTimeFormat('en-us', option).format(timer);
  let time = `${`${timer.getHours()}`.padStart(
      2,
      '0'
    )}:${`${timer.getMinutes()}`.padStart(
      2,
      '0'
    )}: ${`${timer.getSeconds()}`.padStart(2, '0')}`;
  todayShowTime.textContent = formateTimer;
}, 1000);



