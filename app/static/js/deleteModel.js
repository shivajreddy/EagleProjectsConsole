//! Delete community button
const $deleteCommunityButton= $('.modify-community')
$deleteCommunityButton.on('click', delete_community);
async function delete_community(e) {
  e.preventDefault();
  const model_name = 'community';
  const id = e.currentTarget.id;
  const value = e.currentTarget.parentElement.innerText;

  const dialog = confirm(`‼️ THIS ACTION IS NOT REVERSIBLE ‼️ \n Confirm deleting ${value}?`);
  if (dialog) {
    const result = await axios.delete(`/delete/${model_name}/${id}`)
    window.location.assign('/super/new-community')
  }
  else {
    console.log('crysis is averted :)')
  }
};


//! Delete product button
const $deleteProductButton = $('.modify-product')
$deleteProductButton.on('click', delete_product);

async function delete_product(e) {
  e.preventDefault();
  const model_name = 'product';
  const id = e.currentTarget.id;
  const value = e.currentTarget.parentElement.innerText;

  const dialog = confirm(`‼️ THIS ACTION IS NOT REVERSIBLE ‼️ \n Confirm deleting ${value}?`);
  if (dialog) {
    const result = await axios.delete(`/delete/${model_name}/${id}`)
    window.location.assign('/super/products')
  }
  else {
    console.log('crysis is averted :)')
  }
};

//! Delete elevation button
const $deleteElevationButton = $('.modify-elevation')
$deleteElevationButton.on('click', delete_elevation);

async function delete_elevation(e) {
  e.preventDefault();
  const model_name = 'elevation';
  const id = e.currentTarget.id;
  const value = e.currentTarget.parentElement.innerText;

  const dialog = confirm(`‼️ THIS ACTION IS NOT REVERSIBLE ‼️ \n Confirm deleting ${value}?`);
  if (dialog) {
    const result = await axios.delete(`/delete/${model_name}/${id}`)
    window.location.assign('/super/elevations')
  }
  else {
    console.log('crysis is averted :)')
  }
};


//! Delete drafter button
const $deleteDrafterButton = $('.modify-drafter')
$deleteDrafterButton.on('click', delete_drafter);

async function delete_drafter(e) {
  e.preventDefault();
  const model_name = 'drafter';
  const id = e.currentTarget.id;
  const value = e.currentTarget.parentElement.innerText;

  const dialog = confirm(`‼️ THIS ACTION IS NOT REVERSIBLE ‼️ \n Confirm deleting ${value}?`);
  if (dialog) {
    const result = await axios.delete(`/delete/${model_name}/${id}`)
    window.location.assign('/super/drafters')
  }
  else {
    console.log('crysis is averted :)')
  }
};

//! Delete eng button
const $deleteEngButton = $('.modify-eng')
$deleteEngButton.on('click', delete_eng);

async function delete_eng(e) {
  e.preventDefault();
  const model_name = 'eng';
  const id = e.currentTarget.id;
  const value = e.currentTarget.parentElement.innerText;

  const dialog = confirm(`‼️ THIS ACTION IS NOT REVERSIBLE ‼️ \n Confirm deleting ${value}?`);
  if (dialog) {
    const result = await axios.delete(`/delete/${model_name}/${id}`)
    window.location.assign('/super/engineers')
  }
  else {
    console.log('crysis is averted :)')
  }
};


//! Delete plat button
const $deletePlatButton = $('.modify-plat')
$deletePlatButton.on('click', delete_plat);

async function delete_plat(e) {
  e.preventDefault();
  const model_name = 'plat';
  const id = e.currentTarget.id;
  const value = e.currentTarget.parentElement.innerText;

  const dialog = confirm(`‼️ THIS ACTION IS NOT REVERSIBLE ‼️ \n Confirm deleting ${value}?`);
  if (dialog) {
    const result = await axios.delete(`/delete/${model_name}/${id}`)
    window.location.assign('/super/platengineers')
  }
  else {
    console.log('crysis is averted :)')
  }
};


//! Delete jury button
const $deleteJuryButton = $('.modify-jury')
$deleteJuryButton.on('click', delete_jury);

async function delete_jury(e) {
  e.preventDefault();
  const model_name = 'jury';
  const id = e.currentTarget.id;
  const value = e.currentTarget.parentElement.innerText;

  const dialog = confirm(`‼️ THIS ACTION IS NOT REVERSIBLE ‼️ \n Confirm deleting ${value}?`);
  if (dialog) {
    const result = await axios.delete(`/delete/${model_name}/${id}`)
    window.location.assign('/super/jurisdictions')
  }
  else {
    console.log('crysis is averted :)')
  }
};
