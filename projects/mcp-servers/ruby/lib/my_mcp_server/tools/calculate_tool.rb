# frozen_string_literal: true

module MyMcpServer
  module Tools
    # A calculator tool supporting basic arithmetic.
    class CalculateTool
      OPERATIONS = %w[add subtract multiply divide].freeze

      def self.name
        'calculate'
      end

      def self.description
        'Perform basic arithmetic (add, subtract, multiply, divide).'
      end

      def self.schema
        {
          type: 'object',
          properties: {
            operation: {
              type: 'string',
              enum: OPERATIONS,
              description: 'The arithmetic operation to perform'
            },
            a: {
              type: 'number',
              description: 'First operand'
            },
            b: {
              type: 'number',
              description: 'Second operand'
            }
          },
          required: %w[operation a b]
        }
      end

      def self.execute(args)
        op = args['operation']
        a  = args['a'].to_f
        b  = args['b'].to_f

        result = case op
                 when 'add'      then a + b
                 when 'subtract' then a - b
                 when 'multiply' then a * b
                 when 'divide'
                   raise ArgumentError, 'Division by zero' if b.zero?

                   a / b
                 else
                   raise ArgumentError, "Unknown operation: #{op}"
                 end

        # Return integer result when both operands are whole numbers
        result = result.to_i if result == result.to_i

        { result: result, operation: op, a: a, b: b }
      end
    end
  end
end
