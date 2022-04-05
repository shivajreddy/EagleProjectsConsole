//* Auto populate the dates of the form based off Contract date


//? Calculate next N'th work date from given Date
// Helper function to create actual date object from string
function create_date(str_date){
	const splitted = str_date.split('-')
	const year = parseInt(splitted[0])
	const month = parseInt(splitted[1]-1)   // for some weird reason month is being set to given+1, so setting it as -1
	const date = parseInt(splitted[2])
	let today = new Date();
	today.setYear(year);
	today.setMonth(month);
	today.setDate(date);
	return today;
}

// starting from the next day of given day, return the nth working day
function calc_work_date(from_date_str, no_of_days){
	let to_date = create_date(from_date_str);
  while (no_of_days > 0){
    to_date.setDate(to_date.getDate() + 1)
		
    if (to_date.getDay() != 0 && to_date.getDay() != 6){
      no_of_days--;
    }
  }
  return to_date;
}


// event listener for contract date
const contract_date = document.getElementById('contract_date');
contract_date.addEventListener('input', setDates);

const draft_deadline = document.getElementById('draft_deadline');
draft_deadline.setAttribute('disabled', 'disabled');

const eng_planned_receipt = document.getElementById('eng_planned_receipt');
eng_planned_receipt.setAttribute('disabled', 'disabled');

const plat_planned_receipt = document.getElementById('plat_planned_receipt');
plat_planned_receipt.setAttribute('disabled', 'disabled');

const permit_planned_submit = document.getElementById('permit_planned_submit');
permit_planned_submit.setAttribute('disabled', 'disabled');


// event listener for permit received date
const permit_received = document.getElementById('permit_received');
permit_received.addEventListener('input', set_bbp_date);

const bbp_planned_posted = document.getElementById('bbp_planned_posted');
bbp_planned_posted.setAttribute('disabled', 'disabled');


// Get the Contract Date and set other field's dates
function setDates(e){
  const contract_date = e.target.value;

  const draft_date = calc_work_date(contract_date,2);
  const str_draft_date = draft_date.toJSON().slice(0,10);
  draft_deadline.value = str_draft_date;

  const eng_date = calc_work_date(str_draft_date, 10);
  const str_eng_date = eng_date.toJSON().slice(0,10);
  eng_planned_receipt.value = str_eng_date;

  const plat_date = calc_work_date(str_draft_date, 10);
  const str_plat_date = plat_date.toJSON().slice(0,10);
  plat_planned_receipt.value = str_plat_date;

  const permit_date = calc_work_date(str_eng_date, 3);
  const str_permit_date = permit_date.toJSON().slice(0,10);
  permit_planned_submit.value = str_permit_date;

  // console.log(`Dates are contract-> ${contract_date}, draft->${draft_date}, eng->${eng_date}, plat->${plat_date}, permit->${permit_date}, bbp->${bbp_date}`)
};

// set BBP planned date
function set_bbp_date(e){
  const permit_received_date = e.target.value;

  const bbp_date = calc_work_date(permit_received_date, 1);
  const str_bbp_date = bbp_date.toJSON().slice(0,10);
  bbp_planned_posted.value = str_bbp_date;


}

