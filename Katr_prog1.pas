var 
	ammount, number, i, amm_of_found: integer;
	exist : boolean;
	arr: array[1..1000] of integer;

begin 
	exist := False;
	ammount := 0;
	number := 0;
	amm_of_found := 0;
	write ('Введите количество чисел последовательности: ');
	writeln;
	readln(ammount);
	write ('Введите последовательность: ');
	writeln;
	for i := 1 to ammount do begin
		readln(number);
		if (number < 1000) and (number > 99) and (number mod 7 = 0) then begin
			exist := True ;
			arr[1000 -amm_of_found] := number;
			amm_of_found := amm_of_found + 1;
		end;
	end;
	
	writeln;
	if exist = False then begin
		write(-1);
	end;

	for i := 1 to amm_of_found do begin
		write(arr[1000 - amm_of_found + i]);
		writeln;
	end;
end.
