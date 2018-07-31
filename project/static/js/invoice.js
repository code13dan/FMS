function addArticleForm(){
    /* adding another article form */
    // get base DOM elements
    let articlesContainer = document.getElementById('articleFormsContainer'),
        addTrigger = articlesContainer.querySelector('#addArticleForm'),
        cloningBase = articlesContainer.querySelector('.articleForm'),
        articlesCounter = articlesContainer
          .querySelector('#id_form-TOTAL_FORMS');

    // assign click event which will add new article form
    addTrigger.addEventListener('click', addArticle);
    // button event which adds new article form
    function addArticle(event){
        event.preventDefault();
        // create new blank form
        let newForm = cloningBase.cloneNode(true);
            articlesCount = parseInt(articlesCounter.value);
        // increase management form total count
        articlesCounter.setAttribute('value', articlesCount + 1);
        // change new article form Ids to higher number
        changeFormIDs(newForm);
        // display button to remove specific article form and attach event to it
        let deleteTrigger = newForm.querySelector('.removeArticle');
        deleteTrigger.classList.remove('hide');
        deleteTrigger.addEventListener('click', removeArticle);
        // insert new article form right after last form
        let lastArticlePoint = articlesContainer
            .querySelector('#formInsertHere');
        articlesContainer.insertBefore(newForm, lastArticlePoint);
    }

    // assign removeArticle function to buttons
    let deleteTriggers = document.querySelectorAll('.removeArticle');
    for (let i=0; i<deleteTriggers.length; ++i) {
        deleteTriggers[i].addEventListener('click', removeArticle);
    }
    // button event which removes selected article form
    function removeArticle(event){
        event.preventDefault();
        let articlesCount = parseInt(articlesCounter.value),
            thisArticleForm = this.parentElement.parentElement,
            formsToChangeIDs = filterForms(thisArticleForm);
        // decrease management form total count
        articlesCounter.setAttribute('value', articlesCount - 1);
        // change next article forms IDs - by '-1'
        if (formsToChangeIDs){
            formsToChangeIDs.forEach(function(el){
                changeFormIDs(el, 1);
            });
        }

        thisArticleForm.remove();
    }

    // function to change inputs 'name', 'id' and labels 'for' attribute
    function changeFormIDs(formDiv, down=0){
        // default is up
        let shift = down ? -1 : 1,
            inputs = formDiv.querySelectorAll('input, select'),
            labels = formDiv.querySelectorAll('label'),
            idOld = parseInt(labels[0].getAttribute('for').split('-')[1]),
            idNew = down ? idOld + shift : articlesCounter.value - 1;

        for (let i=0; i<inputs.length; i++) {
            let input = inputs[i],
                newId = input.getAttribute('id').replace(idOld, idNew),
                newName = input.getAttribute('name').replace(idOld, idNew);
            input.setAttribute('id', newId);
            input.setAttribute('name', newName);
            // leave 'select' tag value as it is when cloning forms and
            // don't clear inputs when deleting other form
            if ( input.tagName!=='SELECT' && (!(down)) ) {input.value = ''}
        }
        for (let i=0; i<labels.length; i++) {
            let label = labels[i],
                newFor = label.getAttribute('for').replace(idOld, idNew);
            label.setAttribute('for', newFor);
        }
    }
    // return list of next article forms in DOM or return itself
    function filterForms(formDiv){
        function filter(formDiv){
            // return true if formDiv has articleForm class
            if (formDiv.classList.contains('articleForm')) {return formDiv}
        }
        let filteredForms = [];
        while (formDiv = formDiv.nextElementSibling) {
            if (filter(formDiv)) {filteredForms.push(formDiv)} else {break}}
    return filteredForms ? filteredForms : false
    }
}

function searchPartner(){
    /*create and add search functionality to partner part of invoice*/
    let formContainer = document.getElementById('partnerFormContainer'),
        inputCompanyName = formContainer.querySelector('#id_company_name'),
        inputAddress = formContainer.querySelector('#id_address'),
        inputPhone = formContainer.querySelector('#id_phone'),
        inputNIP = formContainer.querySelector('#id_nip'),
        searchList = formContainer.querySelector('#searchList');

    // show or hide search list by toggling 'hide' class
    document.addEventListener('click', showHideSearchList);
    function showHideSearchList(event){
        if ( !(searchList.classList.contains('hide')) ){
            searchList.classList.add('hide');
        } else if ( event.target == inputCompanyName &&
                    searchList.classList.contains('hide') ) {
            searchList.classList.remove('hide');
        }
    }

    // fetch selected partner data and trigger populatePartnerForm function with
    // those data
    searchList.addEventListener('click', fetchPartner);
    function fetchPartner(event){
        if (event.target.matches('p')) {
            let partner_id = event.target.getAttribute('data-id'),
                ajax = new XMLHttpRequest();

            ajax.addEventListener('load', function(){
                let partner = JSON.parse(this.responseText);
                populatePartnerForm(partner);
            });
            ajax.open('GET', 'http://localhost:8000/partners/get/' + partner_id);
            ajax.send();
        }
    }

    // populate partner form with data from fetched partner
    function populatePartnerForm(partner){
        inputCompanyName.value = partner.company_name;
        inputAddress.value = partner.address;
        inputPhone.value = partner.phone;
        inputNIP.value = partner.nip;
    }

    // filter search list of partners with already typed letters
    inputCompanyName.addEventListener('keyup', filterSearchList);
    function filterSearchList(event){
        let typed = inputCompanyName.value,
            partners = searchList.querySelectorAll('p');
        for (let i=0; i<partners.length; i++){
          if (partners[i].innerHTML.toLowerCase().indexOf(typed) > -1){
            partners[i].style.display='';
          }else{
            partners[i].style.display='none';
          }
        }

    }
}

function calculateGrossSum(){
  /* calculate sum of gross valus of all articles */
  let grossSum = document.getElementById('id_amount_gross'),
      articlesContainer = document.getElementById('articleFormsContainer');
  // set gross sum ass readonly input
  grossSum.setAttribute('readonly', true);

  articlesContainer.addEventListener('focusout', addAmounts);
  // when gross amount of article was typed add it to gross sum
  function addAmounts(event){
      if (event.target.getAttribute('name').indexOf('amount_gross') > -1){
        let addValue = event.target.value,
            addAmount = parseInt(addValue) ? parseInt(addValue) : 0,
            oldSum = parseInt(grossSum.value) ? parseInt(grossSum.value) : 0;
        grossSum.value = parseInt(addAmount) + oldSum;
      }
  }

}


addArticleForm();
searchPartner();
calculateGrossSum();