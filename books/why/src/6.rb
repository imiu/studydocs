# def yield_thrice
#   yield
#   yield
#   yield
# end
# 
# a = ['first, birth.', 'then, a life of flickering images.', 'and, finally, the end.']
# yield_thrice { puts a.shift }

# The guts of life force within Dwemthy's Array
class Creature
  # Get a metaclass for this class
  def self.metaclass; class << self; self; end; end

  # Advanced metaprogramming code for nice, clean traits
  def self.traits( *arr )
    return @traits if arr.empty?

    # 1. Set up accessors for each variable
    attr_accessor *arr

    # 2. Add a new class method to for each trait.
    arr.each do |a|
      metaclass.instance_eval do
        define_method( a ) do |val|
          @traits ||= {}
          @traits[a] = val
        end
      end
    end

    # 3. For each monster, the `initialize' method
    #    should use the default number for each trait.
    class_eval do
      define_method( :initialize ) do
        self.class.traits.each do |k,v|
          instance_variable_set("@#{k}", v)
        end
      end
    end

  end

  # Creature attributes are read-only
  traits :life, :strength, :charisma, :weapon
end

class Dragon < Creature
  life( 1340 )     # tough scales
  strength( 451 )  # bristling veins
  charisma( 1020 ) # toothy smile
  weapon( 939 )    # fire breath
end

dr = Dragon.new
p dr