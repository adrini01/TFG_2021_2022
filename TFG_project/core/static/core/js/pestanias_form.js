function cambiarPestanna(pestana, numPestanas) {

    pestania = document.getElementById(pestana.toString());
	cpestana = document.getElementById('c'+pestana.toString());

    for(let i = 2; i <= numPestanas; i++)
	{
		if(i != pestana)
		{
			$(document).ready(function(){
				$(document.getElementById(i.toString())).css('background',"#333333");
				$(document.getElementById(i.toString())).css('padding-bottom','');
				$(document.getElementById('c'+i.toString())).css('display','none');
			});
		}
	}
    $(document).ready(function(){
        $(cpestana).css('display','');
		$(cpestana).css('background', "#333333");
        $(pestania).css('background', "#3ea3f2");
        $(pestania).css('padding-bottom','8px'); 
    });
}