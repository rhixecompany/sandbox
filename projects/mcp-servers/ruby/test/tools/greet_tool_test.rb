# frozen_string_literal: true

require_relative '../test_helper'

class GreetToolTest < Minitest::Test
  def setup
    @tool = MyMcpServer::Tools::GreetTool
  end

  def test_greet_with_name_only
    result = @tool.execute('name' => 'Alice')
    assert_equal 'Hello, Alice!', result[:greeting]
  end

  def test_greet_with_name_and_title
    result = @tool.execute('name' => 'Smith', 'title' => 'Dr.')
    assert_equal 'Hello Dr., Smith!', result[:greeting]
  end

  def test_greet_with_empty_title
    result = @tool.execute('name' => 'Bob', 'title' => '')
    assert_equal 'Hello, Bob!', result[:greeting]
  end

  def test_name_and_description_present
    assert_equal 'greet', @tool.name
    assert @tool.description.is_a?(String)
    refute_empty @tool.description
  end

  def test_schema_is_valid
    schema = @tool.schema
    assert_equal 'object', schema[:type]
    assert_includes schema[:required], 'name'
    assert schema[:properties]['name']
  end
end
