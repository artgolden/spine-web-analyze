var 
	number, max,tmp_max, degree, i: integer;
begin
	max := 0;
	tmp_max := 0;
	write ('Введите число: ');
	readln(number);
	degree := 4096;
	for i := 1 to 7 do begin
		while number >= degree do begin
			number := number - degree;
			tmp_max := tmp_max + 1;
		end;
		if tmp_max > max then 
			max := tmp_max;
		tmp_max := 0;
		degree := degree div 4;
	end;
	write(max);
end.
