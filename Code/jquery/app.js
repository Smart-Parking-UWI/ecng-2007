function readFile()
{
  jQuery.get('test.txt',(txt) => {
    $('#output').text(txt);
  });
}