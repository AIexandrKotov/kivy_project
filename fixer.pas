##
  var KV := KV&<string, string>;
  var replaces := Dict(
    KV(#13#10'Tlgm: @it_boooks', ''),
    KV('«', ''''), KV('»', ''''),
    KV('…… ', '    '), KV('……', '    '),
    KV('… ', '    '), KV('…', ''),
    KV('. ', '.'), KV(' (', '('), KV('’', ''''), KV('"', ''''));
  var fix: string -> string := s -> begin Result := s; foreach var kv in replaces do Result := Result.Replace(kv.Key, kv.Value); end;
  WriteAllText('fixcode.py', fix(ReadAllText('fixcode.py', Encoding.GetEncoding(10007))), Encoding.UTF8);