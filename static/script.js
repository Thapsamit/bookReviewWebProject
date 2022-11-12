
function openNavbar()
{
  const navbarLinks = document.getElementsByTagName('nav')[0];
  navbarLinks.classList.toggle('active');
}

function selectSearchOption()
{

  const searchBook = document.getElementById('search-book');
  const searchBy = document.getElementById('search-by');
  searchBy.setAttribute('placeholder',`Search By ${searchBook.value}`)
}


function editProfile()
{
  const profileInputs = document.querySelectorAll(".profile-inputs");
  const profileSave = document.getElementById("profile-save");

  for(let i = 0; i<profileInputs.length; i++)
  {
    profileInputs[i].disabled = false;
    console.log('test')
  }
  profileInputs[2].disabled = true;
  profileSave.style.display = "inline-block";
 
}

function modalOpen()
{
  const modal = document.getElementById("simple-modal");
  const closeBtn = document.getElementById("closed");
  const btnYes = document.getElementById("btn-yes");
  const btnNo = document.getElementById("btn-no");
  window.addEventListener("click",(e)=>{
    if(e.target == modal)
    {
      modal.style.display = "none";
    } 
  })

  modal.style.display='block';

  closeBtn.addEventListener("click",()=>{
    modal.style.display="none";
  })
  btnYes.addEventListener("click",()=>{
    modal.style.display="none";
  })
  btnNo.addEventListener("click",()=>{
    modal.style.display="none"
  }

)
}

