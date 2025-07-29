private bool _warnedAt5Min = false;
private bool _warnedAt1Min = false;

private void Timer_Tick(object sender, EventArgs e)
{
    if (_user.TimeRemaining.TotalSeconds > 0)
    {
        _user.TimeRemaining -= TimeSpan.FromSeconds(1);
        lblTimeRemaining.Text = _user.TimeRemaining.ToString(@"hh\:mm\:ss");

        // Alerts
        if (_user.TimeRemaining.TotalMinutes <= 5 && !_warnedAt5Min)
        {
            _warnedAt5Min = true;
            ShowAlert("5 minutes remaining!");
        }
        if (_user.TimeRemaining.TotalMinutes <= 1 && !_warnedAt1Min)
        {
            _warnedAt1Min = true;
            ShowAlert("Only 1 minute left!");
        }
    }
    else
    {
        _timer.Stop();
        ShowAlert("Time is up!");
    }
}

private void ShowAlert(string message)
{
    var alert = new UserAlertForm(_user.Username, message);
    alert.ShowDialog();
}
