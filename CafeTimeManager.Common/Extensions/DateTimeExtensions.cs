using System;

namespace CafeTimeManager.Common.Extensions
{
    public static class DateTimeExtensions
    {
        public static bool IsAfter(this DateTime now, DateTime compareTo)
        {
            return now > compareTo;
        }

        public static bool IsBefore(this DateTime now, DateTime compareTo)
        {
            return now < compareTo;
        }

        public static int ToUnixTimestamp(this DateTime date)
        {
            return (int)(date.Subtract(new DateTime(1970, 1, 1))).TotalSeconds;
        }
    }
}
