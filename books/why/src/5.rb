# def dr_chams_timeline( year )
#   case year
#   when 1894
#     "Born." 
#   when 1895..1913
#     "Childhood in Lousville, Winston Co., Mississippi." 
#   when 1914..1919
#     "Worked at a pecan nursery; punched a Quaker." 
#   when 1920..1928
#     "Sailed in the Brotherhood of River Wisdomming, which journeyed \
#      the Mississippi River and engaged in thoughtful self-improvement, \
#      where he finished 140 credit hours from their Oarniversity." 
#   when 1929
#     "Returned to Louisville to pen a novel about time-travelling pheasant hunters." 
#   when 1930..1933
#     "Took up a respectable career insuring pecan nurseries.  Financially stable, he \
#      spent time in Brazil and New Mexico, buying up rare paper-shell pecan trees.  Just \
#      as his notariety came to a crescendo: gosh, he tried to buried himself alive." 
#   when 1934
#     "Went back to writing his novel.  Changed the hunters to insurance tycoons and the \
#      pheasants to Quakers." 
#   when 1935..1940
#     "Took Arthur Cone, the Headmaster of the Brotherhood of River Wisdomming, as a \
#      houseguest.  Together for five years, engineering and inventing." 
#   when 1941
#     "And this is where things got interesting." 
#   else
#     "No information about this year"
#   end
# end
# 
# puts dr_chams_timeline( 1942 )


# noun = 'horus'
# # verb = 'rescued'
#  ['sedated', 'sprinkled', 'electrocuted'].
#  each do |verb|
#    puts "Dr. Cham " + verb + " his niece Hannah. " + noun
#  end
# puts "Yes, Dr. Cham " + verb + " his niece Hannah. " + noun


# class WishMaker
#   def initialize
#     @energy = rand( 6 )
#   end
#   
#   def grant( wish )
#     if wish.length > 10 or wish.include? ' '
#       raise ArgumentError, "Bad wish"
#     end
#     if @energy.zero?
#       raise Exception, "No energy left."
#     end
#     @energy -= 1
#     Endertromb::make( wish )
#   end
# end
# 
# class MindReader
#   def initialize
#     @minds = Endertromb::scan_for_sentience
#   end
#   def read
#     @minds.collect do |mind|
#       mind.read
#     end
#   end
# end


# def wipe_mutterings_from( sentence )
#   unless sentence.respond_to? :include?
#     raise ArgumentError,
#       "cannot wipe mutterings from a #{ sentence.class }"
#   end
#   sentence.gsub( /\([\w]+\)/, '' )
# end
# 
# sent = "And here I am (whispering in the night) on the stage (full of fools)."
# new_sent = wipe_mutterings_from(sent)
# puts sent
# puts new_sent


# class String
#   # The parts of my daughter's organ
#   # instructor's name.
#   @@syllables = [
#     { 'Paij' => 'Personal',
#       'Gonk' => 'Business',
#       'Blon' => 'Slave',
#       'Stro' => 'Master',
#       'Wert' => 'Father',
#       'Onnn' => 'Mother' },
#     { 'ree'  => 'AM',
#       'plo'  => 'PM' }
#   ]
#   # A method to determine what a
#   # certain name of his means.
#   def name_significance
#     parts = self.split( '-' )
#     syllables = @@syllables.dup
#     signif = parts.collect do |p|
#       syllables.shift[p]
#     end
#     signif.join( ' ' )
#   end
# end
# 
# 
# print "Paij-ree".name_significance


# class ArrayMine < Array
#   # Build a string from this array, formatting each entry
#   # then joining them together.
#   def join( sep = $,, format = "%s" )
#     collect do |item|
#       sprintf( format, item )
#     end.join( sep )
#   end
# end
# arr = ArrayMine[1, 2, 3]
# puts arr.join ', ', '%d bed'


class LotteryTicket
  NUMERIC_RANGE = 1..25
  
  attr_reader :picks, :purchased
  
  def initialize( *picks )
    if picks.length != 3
      raise ArgumentError, "three numbers must be picked"
    elsif picks.uniq.length != 3
      raise ArgumentError, "the three picks must be different numbers"
    elsif picks.detect { |p| not NUMERIC_RANGE === p }
      raise ArgumentError, "the three picks must be numbers between 1 and 25."
    end
    @picks = picks
    @purchased = Time.now
  end
end

class LotteryTicket
  def self.new_random
    new(rand(25) + 1, rand(25) + 1, rand(25) + 1)
  rescue ArgumentError
    redo
  end
end

class LotteryTicket
   def score( final )
     count = 0
     final.picks.each do |note|
       count +=1 if picks.include? note
     end
     count
   end
 end

class LotteryDraw
  @@tickets = {}
  def LotteryDraw.buy(customer, *tickets)
    unless @@tickets.has_key?(customer)
      @@tickets[customer] = []
    end
    @@tickets[customer] += tickets
  end
end

class << LotteryDraw
  def play
    final = LotteryTicket.new_random
    winners = {}
    @@tickets.each do |buyer, ticket_list|
      ticket_list.each do |ticket|
        score = ticket.score( final )
        next if score.zero?
        winners[buyer] ||= []
        winners[buyer] << [ ticket, score ]
      end
    end
    @@tickets.clear
    winners
  end
end