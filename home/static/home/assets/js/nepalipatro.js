function NepaliChar() {

    this.englishMonthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'];

    this.nepaliMonthNameEnglish = ['Baisakh', 'Jestha', 'Asar', 'Shrawan', 'Bhadra', 'Ashwin', 'Kartik', 'Mangsir', 'Paush', 'Magh', 'Falgun', 'Chaitra'];

    this.nepaliMonthNames = ['वैशाख', 'जेठ', 'असार', 'साउन', 'भदौ', 'असोज', 'कार्तिक', 'मंसिर', 'पुष', 'माघ', 'फागुन', 'चैत'];

    this.nepaliNumbers = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'];

    this.nepaliWeekDays = ['आइतबार', 'सोमबार', 'मंगलबार', 'बुधबार', 'बिहिबार', 'शुक्रबार', 'शनिबार'];

    this.getNepaliWeekDay = function (day) {
        return this.nepaliWeekDays[day];
    }

    this.getNepaliNumber = function (num) {
        var np_num = '';
        var en_num = num.toString();
        for (let i in en_num) {
            np_num = np_num + this.nepaliNumbers[parseInt(en_num[i])];
        }
        return np_num;
    };


    this.getEnglishDate = function () { return this.englishDate; }

    this.getEngDate = function (month) {
        return this.englishMonthNames[month[0] - 1] + '/' + this.englishMonthNames[month[1] - 1];
    }

};

function DateConverter() {
    this.englishMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    this.englishLeapMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    this.nepaliMonths = [
        [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31], //2000
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30], //2001
        [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [30, 32, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [30, 32, 31, 32, 31, 31, 29, 30, 29, 30, 29, 31],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31],
        [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30], //2071
        [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30], //2072
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31], //2073
        [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],
        [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30],
        [31, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30],
        [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
        [31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30],
        [31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30],
        [31, 32, 31, 32, 30, 31, 30, 30, 29, 30, 30, 30],
        [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30],
        [30, 31, 32, 32, 30, 31, 30, 30, 29, 30, 30, 30],
        [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
        [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30], //2090
        [31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30],
        [30, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30],
        [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
        [31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30],
        [31, 31, 32, 31, 31, 31, 30, 29, 30, 30, 30, 30],
        [30, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30],
        [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30],
        [31, 31, 32, 31, 31, 31, 29, 30, 29, 30, 29, 31],
        [31, 31, 32, 31, 31, 31, 30, 29, 29, 30, 30, 30] //2099
    ];

    this.setCurrentDate = function () {
        var d = new Date();
        this.setEnglishDate(d.getFullYear(), d.getMonth() + 1, d.getDate());
    };


    //English to Nepali date conversion

    this.setEnglishDate = function (year, month, date) {

        if (!this.isEnglishRange(year, month, date))
            throw new Exception("Invalid date format.");

        this.englishYear = year;
        this.englishMonth = month;
        this.englishDate = date;

        //Setting nepali reference to 2000/1/1 with english date 1943/4/14
        this.nepaliYear = 2000;
        this.nepaliMonth = 1;
        this.nepaliDate = 1;

        var difference = this.getEnglishDateDifference(1943, 4, 14);


        //Getting nepali year untill the difference remains less than 365
        var index = 0;

        while (difference >= this.nepaliYearDays(index)) {
            this.nepaliYear++;
            difference = difference - this.nepaliYearDays(index);
            index++;
        }

        //Getting nepali month untill the difference remains less than 31
        var i = 0;
        while (difference >= this.nepaliMonths[index][i]) {
            difference = difference - this.nepaliMonths[index][i];
            this.nepaliMonth++;
            i++;
        }


        //Remaning days is the date;
        this.nepaliDate = this.nepaliDate + difference;


        this.getDay();

    };

    this.toEnglishString = function (format) {
        if (typeof (format) === 'undefined')
            format = "-";
        return this.englishYear + format + this.englishMonth + format + this.englishDate;
    };

    this.getEnglishDateDifference = function (year, month, date) {

        //Getting difference from the current date with the date provided
        var difference = this.countTotalEnglishDays(this.englishYear, this.englishMonth, this.englishDate) - this.countTotalEnglishDays(year, month, date);
        return (difference < 0 ? -difference : difference);

    };

    this.countTotalEnglishDays = function (year, month, date) {
        var totalDays = year * 365 + date;

        for (var i = 0; i < month - 1; i++)
            totalDays = totalDays + this.englishMonths[i];

        totalDays = totalDays + this.countleap(year, month);
        return totalDays;
    };

    this.countleap = function (year, month) {
        if (month <= 2)
            year--;

        return (Math.floor(year / 4) - Math.floor(year / 100) + Math.floor(year / 400));
    };

    this.isEnglishRange = function (year, month, date) {
        if (year < 1944 || year > 2042)
            return false;

        if (month < 1 || month > 12)
            return false;

        if (date < 1 || date > 31)
            return false;

        return true;
    };

    this.isLeapYear = function (year) {
        if (year % 4 === 0) {
            return (year % 100 === 0) ? (year % 400 === 0) : true;
        } else
            return false;
    };


    //Nepali to English conversion

    this.setNepaliDate = function (year, month, date) {
        if (!this.isNepaliRange(year, month, date))
            throw new Exception("Invalid date format.");

        this.nepaliYear = year;
        this.nepaliMonth = month;
        this.nepaliDate = date;

        //Setting english reference to 1944/1/1 with nepali date 2000/9/17
        this.englishYear = 1944;
        this.englishMonth = 1;
        this.englishDate = 1;

        var difference = this.getNepaliDateDifference(2000, 9, 17);

        //Getting english year untill the difference remains less than 365
        while (difference >= (this.isLeapYear(this.englishYear) ? 366 : 365)) {
            difference = difference - (this.isLeapYear(this.englishYear) ? 366 : 365);
            this.englishYear++;
        }

        //Getting english month untill the difference remains less than 31
        var monthDays = this.isLeapYear(this.englishYear) ? this.englishLeapMonths : this.englishMonths;
        var i = 0;
        while (difference >= monthDays[i]) {
            this.englishMonth++;
            difference = difference - monthDays[i];
            i++;
        }

        //Remaning days is the date;
        this.englishDate = this.englishDate + difference;

        this.getDay();

    };

    this.toNepaliString = function (format) {
        if (typeof (format) === 'undefined')
            format = "-";
        return this.nepaliYear + format + this.nepaliMonth + format + this.nepaliDate;
    };

    this.getNepaliDateDifference = function (year, month, date) {

        //Getting difference from the current date with the date provided
        var difference = this.countTotalNepaliDays(this.nepaliYear, this.nepaliMonth, this.nepaliDate) - this.countTotalNepaliDays(year, month, date);
        return (difference < 0 ? -difference : difference);

    };

    this.countTotalNepaliDays = function (year, month, date) {
        var total = 0;
        if (year < 2000)
            return 0;

        total = total + (date - 1);

        var yearIndex = year - 2000;
        for (var i = 0; i < month - 1; i++)
            total = total + this.nepaliMonths[yearIndex][i];

        for (var i = 0; i < yearIndex; i++)
            total = total + this.nepaliYearDays(i);

        return total;
    };

    this.nepaliYearDays = function (index) {
        var total = 0;

        for (var i = 0; i < 12; i++)
            total += this.nepaliMonths[index][i];

        return total;
    };

    this.isNepaliRange = function (year, month, date) {
        if (year < 2000 || year > 2098)
            return false;

        if (month < 1 || month > 12)
            return false;

        if (date < 1 || date > this.nepaliMonths[year - 2000][month - 1])
            return false;

        return true;
    };


    //Class Regular methods

    this.getDay = function () {

        //Reference date 1943/4/14 Wednesday 
        var difference = this.getEnglishDateDifference(1943, 4, 14);
        this.weekDay = ((3 + (difference % 7)) % 7) + 1;
        return this.weekDay;

    };

    this.getEnglishYear = function () { return this.englishYear; };

    this.getEnglishMonth = function () { return this.englishMonth; };

    this.getEnglishDate = function () { return this.englishDate; };

    this.getNepaliYear = function () { return this.nepaliYear; };

    this.getNepaliMonth = function () { return this.nepaliMonth; };

    this.getNepaliDate = function () { return this.nepaliDate; };
};




$.fn.fullCalendar = function (options) {

    $this = $(this);

    // events = [];

    var settings = $.extend({
        events: []
    }, options);



    var converter = new DateConverter();
    converter.setCurrentDate();


    var current_year = parseInt(converter.getNepaliYear());
    var current_month = parseInt(converter.getNepaliMonth());


    var nepChar = new NepaliChar();
    nepaliMonth = nepChar.nepaliMonthNameEnglish;


    englishDateConverter = new DateConverter();

    if ($.isFunction(settings.events)) {
        events = settings.events.call(this, null, null, null, null);
    } else {
        events = settings.events;
    }


    //variables
    var englishDates = [];
    var nepaliEvents = settings.data ? settings.data : [];


    // nepaliEvents = (nepaliEvents.length > 0) ? JSON.parse(nepaliEvents.replace(/&quot;/g, '"')) : [];
    var eventList = [];




    this.each(function () {

        var $calendarElement = $(this);


        var year = current_year;
        var month = current_month;

        converter.setNepaliDate(year, month, 1);
        var start_day = parseInt(converter.getDay());
        var monthEndDay;

        drawCalendar();

        function createWeekHeader() {
            var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

            $tableHeaderTr = $('<div class="npcalendar-weeks"></div>');
            for (let day in days) {
                $header = $('<div class="npcalendar-weeks-name"></div>');
                $header.append('<span>' + nepChar.getNepaliWeekDay(day) + '</span><br>')
                $header.append('<span>' + days[day] + '</span>');
                $tableHeaderTr.append($header);
            }
            return $tableHeaderTr;
        }


        function createMonth(year, month, startDay) {

            console.log("year = ", year)
            $month = $('<div class="npcalendar-days-table"></div>');


            max_days = converter.nepaliMonths[year - 2000][month - 1];

            var dayCounter = 1;
            var counter = 1;

            nepali_events = nepaliEvents;
            week = 1;
            while (max_days > counter - startDay) {
                $week = $('<div class="npcalendar-days week-' + week + '"></div>');

                $week.append(eventsTable);

                for (var i = 0; i < 7; i++) {

                    if (counter >= startDay && max_days > counter - startDay) {
                        englishDateConverter.setNepaliDate(year, month, dayCounter);

                        eng_date = englishDateConverter.getEnglishDate();
                        eng_month = englishDateConverter.getEnglishMonth();
                        eng_year = englishDateConverter.getEnglishYear();

                        if (englishDates.includes(eng_month) === false) {
                            englishDates.push(eng_month);
                        }

                        var currentEvent;


                        if (counter % 7 == 0) {

                            if (currentEvent = checkEvents(eng_year, eng_month, eng_date)) {


                                $day = createDay(dayCounter, eng_date, eng_month, eng_year);

                                $day.addClass('npcalendar-days-holiday')
                                $day.data('event', currentEvent);
                                $week.append($day);

                                eventList.push(...setEvent(currentEvent, i, week, events));

                            } else {
                                $day = createDay(dayCounter, eng_date, eng_month, eng_year)
                                $day.addClass('npcalendar-days-holiday')
                                $week.append($day);

                            }
                        } else {

                            if (currentEvent = checkEvents(eng_year, eng_month, eng_date)) {

                                $day = createDay(dayCounter, eng_date, eng_month, eng_year);
                                $day.data('event', currentEvent);
                                $week.append($day);
                                eventList.push(...setEvent(currentEvent, i, week, events));

                            } else {
                                $day = createDay(dayCounter, eng_date, eng_month, eng_year)
                                $week.append($day);
                            }
                        }

                        dayCounter++;

                        if (events.length > 0) {
                            if (dayCounter > max_days) {

                                eng_month = (eng_month < 10) ? "0" + eng_month : eng_month
                                eng_date = eng_date < 10 ? "0" + eng_date : eng_date;
                                monthEndDay = formatDate(convertDateToFormat(eng_year, eng_month, eng_date))
                            }
                        }

                    } else {
                        $day = createDay('', '', '', '', '', '', '');
                        $day.addClass('disabled')
                        $week.append($day);
                    }

                    counter++;

                }
                $month.append($week);
                week++;

            }
            return $month;
        }

        function getDaysRequired(event) {

            var from = event.start ? new Date(event.start) : null;
            var to = event.end ? new Date(event.end) : null;

            if (to) {
                return getDateDifference(from, to);
            }

            return 1;

        }

        function getDateDifference(from, to) {
            var difference = Math.abs(to - from);
            var daysDiff = Math.ceil(difference / (1000 * 60 * 60 * 24));
            return daysDiff
        }


        function createDate(date) {
            var yyyy = date.getFullYear();
            var mm = date.getMonth() + 1;
            var dd = date.getDate();

            return formatDate(convertDateToFormat(yyyy, mm, dd));
        }

        function eventsTable() {
            $eventTable = $('<div class="events-table"></div>');
            $eventTable.append($('<div class="events-table-1"></div>'));
            $eventTable.append($('<div class="events-table-2"></div>'));


            return $eventTable;
        }

        function checkEvents(eng_year, eng_month, eng_date) {

            var dates;
            var eventList = [];
            for (var i = 0; i < events.length; i++) {
                try {
                    dates = events[i].start.split('-')
                    if (parseInt(dates[0]) == eng_year && parseInt(dates[1]) == eng_month && parseInt(dates[2]) == eng_date) {
                        // return events[i];
                        eventList.push(events[i]);
                    }
                } catch (e) {

                }
            }

            if (eventList.length === 0) {
                return false;
            }

            return eventList;

        }

        function convertDateToFormat(year, month, day) {
            return year + "-" + month + "-" + day;
        }

        function formatDate(date) {
            var temp_date = date.split("-")
            var month = parseInt(date.split("-")[1]);
            var day = parseInt(date.split("-")[2]);

            temp_date[1] = (month / 10) < 1 ? "0" + month : month;
            temp_date[2] = (day / 10) < 1 ? "0" + day : day;
            return temp_date.join("-");
        }

        function createDay(dayCounter, engDay, eng_month, eng_year) {

            today = new Date();

            if (engDay !== '') {
                var fullDate = formatDate(convertDateToFormat(eng_year, eng_month, engDay))
            } else {
                var fullDate = null
            }

            $day = $('<div class="npcalendar-days-count" data-date=' + fullDate + '></div>');

            if (today.getMonth() + 1 == eng_month && today.getDate() == engDay && today.getFullYear() == eng_year) {
                $day.addClass('npcalendar-date-today');
            }


            $day.append(getNepDay(nepChar.getNepaliNumber(dayCounter)));


            $day.append(getEnglishDay(engDay, fullDate));

            return $day;
        }

        function getEnglishEvent(event) {

            e = $('<span class="npcalendar-english-event"></span>');
            return e;
        }


        function getNepaliEvents(event) {
            return $('<span class="npcalendar-event">' + event + '</span>');

        }

        function getNepDay(day) {
            return $('<span class="npcalendar-nep-days npcalendar-nep-days-e">' + day + '</span>');
        }

        function getTithi(tithi) {
            return $('<span class="npcalendar-tithi">' + tithi + '</span>');
        }

        function getEnglishDay(engDay, fullDate) {
            //     return $(`<div class="fc-day-top" data-date="${fullDate}">
            //     <span class="npcalendar-eng-days">${engDay}</span>
            //     <span class="fc-day-number></span>
            // </div>`)
            return $(`<span class="npcalendar-eng-days fc-day-top" data-date="${fullDate}">${engDay}</span>`);
        }

        function createNavigation() {
            $npCalendarNextPrev = $('<div class="npcalendar-next-prev"></div>');
            $npCalendarNextPrev.append(getNepaliDateLeft);
            $npCalendarNextPrev.append(getNpCalendarArrow);
            $npCalendarNextPrev.append(getEnglishDateRight);
            return $npCalendarNextPrev;
        }

        function getNepaliDateLeft() {

            return $(`
                <div class="npcalendar-nepali-date">
                    <button type="button" class="npcalendar-btn">${nepChar.nepaliMonthNameEnglish[month - 1]} ${year}</button>
                </div>
            `);
        }

        function getNpCalendarArrow() {
            $npCalendarArrow = $('<div class="npcalendar-arrow"></div>');
            $npCalendarArrow.append(getPrevBtn);
            $npCalendarArrow.append(getSelectYear);
            $npCalendarArrow.append(getSelectMonth);
            $npCalendarArrow.append(getNextBtn);
            return $npCalendarArrow;
        }

        function getPrevBtn() {

            return `
                <button class="npcalendar-prev npcalendar-prev-btn">
                    <img src="https://img.icons8.com/material-rounded/24/000000/back.png">
                </button>
            `;
        }

        function getNextBtn() {

            return `
                <button class="npcalendar-next npcalendar-next-btn">
                    <img src="https://img.icons8.com/material-rounded/24/000000/forward.png">
                </button>
            `
        }

        function getEnglishDateRight() {

            return $(
                `
                    <div class="npcalendar-date">
                        <button type="button" class="npcalendar-btn"></button>
                    </div>
                `
            );
        }

        function getSelectYear() {
            nepaliMonths = nepChar.nepaliMonthNames;
            $select = $('<select class="form-control npcalendar-years npcalendar-btn" id="id_year" name="year"></select>');
            for (var i = 2071; i <= 2080; i++) {
                $option = $('<option value=' + i + '>' + nepChar.getNepaliNumber(i) + '</option>');
                $select.append($option);
            }
            return $select;
        }

        function getSelectMonth() {
            $select = $('<select class="form-control npcalendar-months npcalendar-btn" id="id_month" name="month"></select>');
            for (let d in nepaliMonths) {
                val = parseInt(d) + 1;
                $option = $('<option value=' + val + '>' + nepaliMonths[d] + '</option>');
                $select.append($option);
            }
            return $select;
        }

        function drawCalendar() {
            $calendarElement.empty();


            $npContainer = $('<div class="np-container text-center"></div>');
            $npCalendar = $('<div class="npcalendar"></div>');


            /* Navigation */
            $nav = $npCalendar.append(createNavigation);

            /* Week Header */
            $weekHeader = $npCalendar.append(createWeekHeader);

            /* Month */
            $month = $npCalendar.append(createMonth(year, month, start_day));

            $npContainer.append($weekHeader);
            $npContainer.append($month);
            $npContainer.append($nav);



            $calendarElement.append($npContainer);
            $npCalendar.find('.npcalendar-months').val(month);
            $npCalendar.find('.npcalendar-years').val(year);

            $nextBtn = $npCalendar.find('.npcalendar-next');
            $nextBtn.on('click', next);

            $prevBtn = $npCalendar.find('.npcalendar-prev');
            $prevBtn.on('click', prev);

            $npCalendar.find('.npcalendar-date').find('button').html(nepChar.getEngDate(englishDates) + " " + converter.getEnglishYear());
            //set englishDates to empty list for new month


            /* Events */
            $npCalendar.find('.npcalendar-months').change(function () {
                month = $(this).val();
                calendarChange();
            });

            $npCalendar.find('.npcalendar-years').change(function () {
                year = $(this).val();
                calendarChange();
            });



            $npCalendar.find('.npcalendar-days-count').on('click', dayClick);

            setNepaliEvents($npCalendar);


            var new_event_list = getNewEvents();
            partitionEvents(new_event_list, $npCalendar);

            $npCalendar.find('.event-flex').on('click', function () {
                eventClick($(this).data('event'));
            });

            $npCalendar.find('.events').click(function (e) {
                e.stopPropagation();
                console.log('show more')
                showMore($(this).data('events'))
            });

            $npCalendar.find('.events-2').click(function (e) {
                e.stopPropagation();
                console.log('show more')
                showMore($(this).data('events'))
            });

            eventList = [];
            englishDates = [];
            /* End Events*/
        }

        function next() {

            if (month == 12 && year == 2098) {
                return;
            }

            month++;
            if (month > 12) {
                year++;
                month = 1;
            }
            calendarChange();
        }

        function prev() {


            if (month == 1 && year == 2000) {
                return;
            }

            month--;
            if (month < 1) {
                year--;
                month = 12;
            }
            calendarChange();
        }

        function calendarChange() {
            converter.setNepaliDate(year, month, 1);
            start_day = parseInt(converter.getDay());
            drawCalendar();
        }


        /* Events */
        eventClick = function (event) {
            if (event && typeof (event) !== 'undefined') {

                if ($.isFunction(settings.eventClick)) {
                    settings.eventClick.call(this, event, null, null);
                } else {
                    console.log("ok " + event);
                }
            } else {
                console.log("aasdf")
            }
        }

        function dayClick() {

            var date = new Date($(this).data('date'));

            if ($.isFunction(settings.dayClick)) {
                settings.dayClick.call(this, date.toISOString(), null, null);
            } else {
                console.log("date = " + date);
            }
        }



        showMore = function (event) {
            if ($.isFunction(settings.showMore)) {
                settings.showMore.call(this, event);
            } else {
                console.log("show more")
                console.log(event);
            }
        }

        function eventRender(event, element) {
            if ($.isFunction(settings.eventRender)) {
                settings.eventRender.call(this, event, element);
            } else {
                console.log("event rendered")
            }
        }

        function dayRender(date, cell) {
            if ($.isFunction(settings.dayRender)) {
                settings.dayRender.call(this, date, cell);
            }
        }

        function setNepaliEvents(current_div) {
            for (var i = 1; i < 7; i++) {
                // $week = $('.week-' + i + '')
                $week = current_div.find($(`.week-${i}`))
                $week.children().each(function (e, i) {
                    var date = $(this).data('date')
                    if (date) {
                        dayRender(moment(date, "YYYY MM DD"), i);
                        for (var j = 0; j < nepaliEvents.length; j++) {
                            var event_date = nepaliEvents[j].english_date;
                            if (formatDate(event_date) === date) {
                                var event = nepaliEvents[j].event ? nepaliEvents[j].event : '';
                                var tithi = nepaliEvents[j].tithi ? nepaliEvents[j].tithi : '';
                                var holiday = nepaliEvents[j].holiday ? nepaliEvents[j].holiday : false;
                                $(this).append(getNepaliEvents(event))
                                $(this).append(getTithi(tithi))
                                if (holiday) {
                                    $(this).addClass('npcalendar-days-holiday')
                                }
                            }
                        }

                    }
                });
            }
        }

        function setEvent(event, start, week, events) {


            var tempList = [];


            for (var i = 0; i < event.length; i++) {

                dateObj = {};
                dates = []
                if (event[i].end) {

                    start_date = new Date(event[i].start);
                    end_date = new Date(event[i].end);

                    for (var d = start_date; d <= end_date; d.setDate(d.getDate() + 1)) {
                        date = new Date(d);

                        dates.push(createDate(date));
                    }
                    dateObj['id'] = event[i].id ? event[i].id : null
                    dateObj['dates'] = dates
                    dateObj['status'] = event[i].status ? event[i].status : false
                    dateObj['title'] = event[i].title
                    dateObj['start'] = start
                    dateObj['week'] = week
                    dateObj['index'] = events.indexOf(event[i])
                    dateObj['backgroundColor'] = event[i].backgroundColor ? event[i].backgroundColor : '';
                    dateObj['textColor'] = event[i].textColor ? event[i].textColor : '';
                    dateObj['borderColor'] = event[i].borderColor ? event[i].borderColor : '';
                    dateObj['description'] = event[i].description ? event[i].description : '';
                    dateObj['reporter'] = event[i].reporter ? event[i].reporter : '';
                    dateObj['in_progress'] = event[i].in_progress ? event[i].in_progress : false;
                    dateObj['is_completed'] = event[i].is_completed ? event[i].is_completed : false;
                } else {

                    dates.push(createDate(new Date(event[i].start)))
                    dateObj['id'] = event[i].id ? event[i].id : null
                    dateObj['dates'] = dates;
                    dateObj['status'] = event[i].status ? event[i].status : false
                    dateObj['title'] = event[i].title
                    dateObj['start'] = start
                    dateObj['week'] = week
                    dateObj['index'] = events.indexOf(event[i])
                    dateObj['backgroundColor'] = event[i].backgroundColor ? event[i].backgroundColor : '';
                    dateObj['textColor'] = event[i].textColor ? event[i].textColor : '';
                    dateObj['borderColor'] = event[i].borderColor ? event[i].borderColor : '';
                    dateObj['description'] = event[i].description ? event[i].description : '';
                    dateObj['reporter'] = event[i].reporter ? event[i].reporter : '';
                    dateObj['in_progress'] = event[i].in_progress ? event[i].in_progress : false;
                    dateObj['is_completed'] = event[i].is_completed ? event[i].is_completed : false;

                }

                tempList.push(dateObj);
            }
            return tempList;
        }

        function arraysEqual(arr1, arr2) {
            if (arr1.length !== arr2.length)
                return false;
            for (var i = arr1.length; i--;) {
                if (arr1[i] !== arr2[i])
                    return false;
            }

            return true;
        }

        function sortEvents(events) {
            var temp_events = [...events]
            for (var i = 0; i < temp_events.length; i++) {
                for (var j = 0; j < temp_events.length - i - 1; j++) {
                    if (temp_events[j].dates.length < temp_events[j + 1].dates.length) {
                        var temp = temp_events[j];
                        temp_events[j] = temp_events[j + 1];
                        temp_events[j + 1] = temp;
                    }
                }
            }

            return temp_events;
        }

        function filter_events(events) {
            var day_taken = [];
            var week_events = [];

            for (var i = 0; i < events.length; i++) {
                var dates_from_event = events[i].dates;
                var start_date = events[i].dates[0];
                if (!day_taken.includes(start_date)) {
                    week_events.push(events[i]);
                }
                day_taken.push(...dates_from_event);
            }

            return week_events;
        }

        function calculateHoliday(date, event1, event2) {
            if (typeof (event1) === "undefined") {
                return event2.start;
            } else {
                var last_date_event_1 = event1.dates[event1.dates.length - 1];
                var start_date_event_2 = event2.dates[0];
                var difference = getDateDifference(new Date(start_date_event_2), new Date(last_date_event_1))
                return difference - 1;
            }
        }

        function setCss(element, days) {
            $(element).find('.npcalendar-nep-days').addClass('has-event')
            $(element).find('.npcalendar-tithi').hide();
            var curr = $(element);
            for (var i = 0; i < days - 1; i++) {
                $(curr).next().find('.npcalendar-nep-days').addClass('has-event')
                $(curr).find('.npcalendar-tithi').hide();
                curr = $(curr).next()
            }
        }

        function setWeekEvents(event, week, event_div, current_div) {
            // console.log(week);
            var sorted_events = sortEvents(event);

            $week = current_div.find($(`.week-${week}`));

            var totalSpan = 0;

            var filtered_events = filter_events(sorted_events);
            // console.log("filtered = ", filtered_events)
            var weekendDay = $week.children().last().data('date');
            var available_days = 7 - totalSpan;
            var prev_events = [];
            var isWeekend = false;
            $week.children().each(function () {

                var date = $(this).data('date');
                var day = $(this);

                if (date) {
                    filtered_events.forEach((e, i) => {
                        var start_date = e.dates[0];
                        if (date === formatDate(start_date)) {
                            var ev = prev_events.pop()
                            var holiday = calculateHoliday(date, ev, e);
                            for (var z = 0; z < holiday; z++) {
                                $week.find(event_div).append($('<div class="event-gap"></div>'))
                                available_days--;
                            }
                            var totalDays = e.dates.length;

                            $e = $(`
                                <div class="event-flex flex-${totalDays}" style="background:${e.backgroundColor};border-color:${e.borderColor};">
                                    <span style="color:${e.textColor};position: absolute;left: 50%;top: 50%;font-size: 12px;transform: translate(-50%, -50%);width: 100%;text-overflow: ellipsis;white-space: nowrap;overflow: hidden;line-height: 16px;">
                                        ${e.title}
                                    </span>
                                </div>`);
                            $e.data('event', e);
                            $d = $(this).parent().find(event_div).append($e)
                            available_days -= totalDays;
                            prev_events.push(e);
                            eventRender(e, $e.find('span'));
                            setCss(day, totalDays);
                        }
                    });
                    if (weekendDay === date && available_days !== 0) {
                        for (var j = 0; j < available_days; j++) {
                            $week.find(event_div).append($('<div class="event-gap"></div>'))
                        }
                    }
                    if (!weekendDay) {
                        isWeekend = true;
                    }

                }
            });
            if (isWeekend && available_days !== 0) {
                for (var j = 0; j < available_days; j++) {
                    $week.find(event_div).append($('<div class="event-gap"></div>'))
                }
            }

        }

        // if event's  length is greater than a week
        function getNewEvents() {
            var temp_event_list = eventList.slice();

            var max_week = $('.week-6').length === 1 ? 6 : 5;
            for (var i = 1; i < 7; i++) {


                eventList.filter(function (e) {
                    var weekendDay = $('.week-' + i + '').children().last().data('date')
                    if (e.week == i) {

                        if (weekendDay) {

                            var month_end_day = createDate(new Date(monthEndDay));

                            var newEventsTempList = [];
                            for (var j = 0; j < e.dates.length; j++) {
                                if (e.dates[j] === weekendDay) {
                                    event1 = {
                                        'id': e.id ? e.id : null,
                                        'dates': e.dates.slice(0, j + 1),
                                        'title': e.title,
                                        'start': e.start,
                                        'week': e.week,
                                        'backgroundColor': e.backgroundColor,
                                        'index': e.index,
                                        'textColor': e.textColor,
                                        'borderColor': e.borderColor,
                                        'status': e.status,
                                        'description': e.description,
                                        'reporter': e.reporter,
                                        'status': e.status,
                                        'in_progress': e.in_progress,
                                        'is_completed': e.is_completed

                                    }

                                    var new_week = (e.week + 1 > max_week) ? 1 : e.week + 1;

                                    event2 = {
                                        'id': e.id ? e.id : null,
                                        'dates': e.dates.slice(j + 1, e.dates.length),
                                        'title': e.title, 'start': 0,
                                        'week': new_week,
                                        'backgroundColor': e.backgroundColor,
                                        'index': e.index,
                                        'textColor': e.textColor,
                                        'borderColor': e.borderColor,
                                        'status': e.status,
                                        'description': e.description,
                                        'reporter': e.reporter,
                                        'status': e.status,
                                        'in_progress': e.in_progress,
                                        'is_completed': e.is_completed
                                    }
                                    newEventsTempList.push(event1)


                                    if (event2.dates.length > 0) {
                                        var d1 = new Date(event2.dates[0])
                                        var d2 = new Date(month_end_day);


                                        if (d1 < d2) {

                                            newEventsTempList.push(event2)
                                        } else {

                                            var new_obj = { 'title': event2.title, 'start': event2.dates[0], 'end': event2.dates[event2.dates.length - 1] }

                                            if (!checkObjExists(new_obj)) {
                                                events.push(new_obj)
                                            }
                                        }
                                    }
                                }
                            }

                            if (newEventsTempList.length > 0) {
                                var index = temp_event_list.indexOf(e)
                                temp_event_list.splice(index, 1, ...newEventsTempList)
                            }


                        }


                    }
                });


                var new_temp_event_list = temp_event_list.slice();
                for (var j = 0; j < new_temp_event_list.length; j++) {
                    if (new_temp_event_list[j].dates.length > 7) {
                        var newEvents = breakEvent(new_temp_event_list[j], i, max_week);
                        new_temp_event_list.splice(j, 1, ...newEvents)
                    }
                }
            }
            return new_temp_event_list;
        }


        //splits events into weeks
        function breakEvent(event, week, max_week) {
            var dates = event.dates;
            var start = 0;
            var end = 7;
            var tmpEventLists = [];
            var week = event.week;

            if (week === max_week) {
                return [event];
            }

            for (var i = 0; i < Math.ceil(dates.length / 7); i++) {
                var obj = {};

                var date = dates.slice(start, end);
                obj['id'] = event.id ? event.id : null
                obj['dates'] = date;
                obj['title'] = event.title;
                obj['start'] = event.start;
                obj['week'] = week;
                obj['index'] = event.index
                obj['backgroundColor'] = event.backgroundColor;
                obj['borderColor'] = event.borderColor;
                obj['textColor'] = event.textColor;
                obj['status'] = event.status;
                obj['description'] = event.description;
                obj['reporter'] = event.reporter;
                obj['status'] = event.status
                obj['in_progress'] = event.in_progress
                obj['is_completed'] = event.is_completed

                tmpEventLists.push(obj);

                week++;
                start += 7;
                end += 7;

            }

            return tmpEventLists;

        }

        //splits events into event-1 or event-2
        function partitionEvents(partitionEventsEventList, current_div) {
            var month_offset_list = checkMonthOffset(partitionEventsEventList);
            for (var i = 1; i < 7; i++) {
                var tmpEvents = [];
                month_offset_list.filter(function (e) {
                    if (e.week === i && e.dates.length > 0) {
                        tmpEvents.push(e);
                    }
                });

                var events1 = [];
                var events2 = [];

                if (tmpEvents.length > 0) {

                    events1.push(tmpEvents[0]);
                    var lastdate = formatDate(tmpEvents[0].dates[tmpEvents[0].dates.length - 1])
                    for (var j = 1; j < tmpEvents.length; j++) {
                        startdate = formatDate(tmpEvents[j].dates[0])
                        var d1 = new Date(lastdate);
                        var d2 = new Date(startdate);

                        if (d1 >= d2) {
                            // events2.push(events[j]);

                            if (events2.length > 0) {
                                events2_last_date = events2[events2.length - 1].dates[events2[events2.length - 1].dates.length - 1]
                                current_event_start_date = tmpEvents[j].dates[0]

                                if (events2_last_date >= current_event_start_date) {
                                    events1.push(tmpEvents[j])
                                } else {
                                    events2.push(tmpEvents[j]);
                                }
                            } else {
                                events2.push(tmpEvents[j]);
                            }
                        } else {
                            // events1.push(events[j]);

                            if (events1.length > 0) {
                                events1_last_date = events1[events1.length - 1].dates[events1[events1.length - 1].dates.length - 1]
                                current_event_start_date = tmpEvents[j].dates[0]

                                if (events1_last_date >= current_event_start_date) {
                                    events2.push(tmpEvents[j])
                                } else {
                                    events1.push(tmpEvents[j]);
                                }
                            } else {
                                events1.push(tmpEvents[j]);
                            }
                        }
                        lastdate = tmpEvents[j].dates[tmpEvents[j].dates.length - 1]

                    }
                }

                setWeekEvents(events1, i, '.events-table-1', current_div)
                setWeekEvents(events2, i, '.events-table-2', current_div)
                console.log("events1 =", events1);
                console.log("events2 = ", events2);
                console.log('----------------------------------------')
                var overlapped1 = getOverlappingEvents(events1);
                var overlapped2 = getOverlappingEvents(events2);

                setOverlappingEvents(overlapped1, i, current_div);
                setOverlappingEvents(overlapped2, i, current_div);


            }


        }

        function setOverlappingEvents(event, week, current_div) {


            $week = current_div.find($(`.week-${week}`));

            $week.children().each(function () {
                var current_date = $(this).data('date');
                var temp_list = [];

                if (current_date) {
                    for (var i = 0; i < event.length; i++) {
                        for (var j = 0; j < event[i].dates.length; j++) {
                            var event_date = event[i].dates[j];
                            if (event_date === current_date) {
                                temp_list.push(event[i]);
                            }
                        }

                    }

                    if (temp_list.length > 0) {
                        $d = $('<a class="events"> + ' + temp_list.length + '</a>');
                        var e = temp_list.length + 1;

                        $e = $('<a class="events-2"> + ' + e + '</a>');
                        $e.data('events', temp_list)
                        $d.data('events', temp_list)

                        $(this).append($d);
                        $(this).append($e);
                    }


                }
            });


        }

        function getOverlappingEvents(event) {

            temp_event = event.slice();


            var overlapped = [];

            for (var i = 0; i < event.length; i++) {

                var curr_event = event[i];
                var start_date = new Date(curr_event.dates[0]);
                var end_date = new Date(curr_event.dates[curr_event.dates.length - 1]);

                for (var j = i + 1; j < event.length; j++) {
                    var event_date = new Date(event[j].dates[0])
                    if (event_date >= start_date && event_date <= end_date) {
                        const found = overlapped.some(el => el === event[j])
                        if (!found) {
                            overlapped.push(event[j])
                        }
                    }
                }

            }
            return overlapped;
        }


        /* 
            checks if event lies between two dates
            if it does splits the date into two months
         
        */
        function checkMonthOffset(monthOffsetEventList) {
            var new_temp_list = [...monthOffsetEventList]

            for (var i = 0; i < new_temp_list.length; i++) {
                var d1 = new Date(new_temp_list[i].dates[new_temp_list[i].dates.length - 1])
                var d2 = new Date(monthEndDay);

                if (d1 >= d2) {
                    var new_events = setNextMonthEvent(new_temp_list[i], d2);
                    new_events[0]['new_date'] = 'this';
                    new_temp_list.splice(i, 1, ...[new_events[0]])


                    if (!checkObjExists(new_events[1])) {
                        events.push(new_events[1])
                    }

                }
            }
            return new_temp_list;

        }

        function checkObjExists(obj) {

            for (var i = 0; i < events.length; i++) {
                if (JSON.stringify(obj) === JSON.stringify(events[i])) {
                    return true;
                }
            }

            return false;
        }

        function addOneDay(date, day = 1) {
            date.setDate(date.getDate() + day)
            return date

        }

        function convertDate(date) {
            var temp_date = date.split("-")
            var month = parseInt(date.split("-")[1]);
            if ((month / 10) < 1) {
                var temp_month = "0" + month
                temp_date[1] = temp_month
                return new Date(temp_date.join("-"))

            } else {
                return new Date(date)
            }

        }

        function setNextMonthEvent(event, lastDay) {
            var temp = [];


            var d1 = getDateDifference(new Date(lastDay), convertDate(event.dates[0]))
            var d2 = getDateDifference(convertDate(event.dates[event.dates.length - 1]), new Date(lastDay))
            dates1 = event.dates.slice(0, d1 + 1)
            // var dates1 = event.dates.slice(0, d1)

            var dates2 = event.dates.slice(d1 + 1, event.dates.length)
            //set event for current month
            temp.push({
                'id': event.id ? event.id : null,
                'dates': dates1,
                'title': event.title,
                'start': event.start,
                'week': event.week,
                'backgroundColor': event.backgroundColor,
                'index': event.index,
                'borderColor': event.borderColor,
                'textColor': event.textColor,
                'description': event.description,
                'reporter': event.reporter,
                'status': event.status,
                'in_progress': event.in_progress,
                'is_completed': event.is_completed
            })

            //sets event for next month
            temp.push({
                'id': event.id ? event.id : null,
                'title': event.title,
                'start': dates2[0],
                "end": dates2[dates2.length - 1],
                'backgroundColor': event.backgroundColor,
                'borderColor': event.borderColor,
                'textColor': event.textColor,
                'description': event.description,
                'reporter': event.reporter,
                'status': event.status,
                'in_progress': event.in_progress,
                'is_completed': event.is_completed

            })
            return temp;

        }
    });



};