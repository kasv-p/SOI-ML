function csrc()
{
  if (document.getElementById("videoInput").src != "")
  {
    document.getElementById("videoInput").src = "";
  }
  else
  {
    document.getElementById("videoInput").src="{{ url_for('video') }}";
  }
}
