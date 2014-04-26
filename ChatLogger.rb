
require 'isaac'

configure do |c|
  c.nick    = ""
  c.server  = "199.9.252.26"
  c.password = "oauth:duz"
  c.port    = 6667
end

on :connect do
  join "#twitchplayspokemon"
end



on :channel, /.*/ do
  open("#{channel}4.log", "a") do |log|
		time = Time.new
    current = "<date>" + time.year.to_s + "-" + time.month.to_s + "-" + time.day.to_s + "</date><time>" + time.hour.to_s  + ":" + time.min.to_s  + ":" + time.sec.to_s + ":" + time.usec.to_s + "</time>"
    log.puts current + "<user>#{nick}</user><msg>#{message}</msg>"
  end

  #puts "#{channel}: #{nick}: #{message}"
end
